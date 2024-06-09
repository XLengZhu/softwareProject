from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.models import User, Administrator, Classroom, ClassroomUsage

@app.route('/register/user', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')  # 修改这里
    new_user = User(id=data['id'], name=data['name'], password=hashed_password, permission=data.get('permission', False))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'code':201,'message': 'New user registered successfully'})

@app.route('/register/admin', methods=['POST'])
def register_admin():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')  # 修改这里
    new_admin = Administrator(id=data['id'], name=data['name'], password=hashed_password)
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({'code':201,'message': 'New administrator registered successfully'})

@app.route('/login/user', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(id=data['id']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'code':401,'message': 'Login failed, please check your ID and password'})
    return jsonify({'code':200,'message': 'Login successful', 'id': user.id, 'name': user.name, 'permission': user.permission})

@app.route('/login/admin', methods=['POST'])
def login_admin():
    data = request.get_json()
    admin = Administrator.query.filter_by(id=data['id']).first()
    if not admin or not check_password_hash(admin.password, data['password']):
        return jsonify({'code':401,'message': 'Login failed, please check your ID and password'})
    return jsonify({'code':200,'message': 'Login successful', 'id': admin.id, 'name': admin.name})

# 所有教室查询
@app.route('/classrooms', methods=['GET'])
def get_classrooms():
    classrooms = Classroom.query.all()
    return jsonify([{'id': c.id, 'location': c.location, 'capacity': c.capacity, 'type': c.type} for c in classrooms])

# 教室信息增加
@app.route('/classrooms', methods=['POST'])
def add_classroom():
    data = request.get_json()
    new_classroom = Classroom(id=data['id'], location=data['location'], capacity=data['capacity'], type=data['type'])
    db.session.add(new_classroom)
    db.session.commit()
    return jsonify({'message': 'Classroom added successfully'}), 201

# 教室信息删除
@app.route('/classrooms/<string:classroom_id>', methods=['DELETE'])
def delete_classroom(classroom_id):
    classroom = Classroom.query.get(classroom_id)
    if not classroom:
        return jsonify({'message': 'Classroom not found'}), 404
    db.session.delete(classroom)
    db.session.commit()
    return jsonify({'message': 'Classroom deleted successfully'}), 200

# 教室状态信息更改
@app.route('/classrooms/usage', methods=['POST'])
def change_classroom_status():
    data = request.get_json()
    start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
    new_usage = ClassroomUsage(
        classroom_id=data['classroom_id'],
        start_time=start_time,
        end_time=end_time,
        occupier_id=data['occupier_id']
    )
    db.session.add(new_usage)
    db.session.commit()
    return jsonify({'code':201,'message': 'Classroom usage added successfully'})

# 用户权限信息更改
@app.route('/users/<string:user_id>/permission', methods=['PUT'])
def change_user_permission(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'code':404,'message': 'User not found'})
    user.permission = data['permission']
    db.session.commit()
    return jsonify({'code':200,'message': 'User permission updated successfully'})

# 查询用户预订
@app.route('/user/<string:user_id>/bookings', methods=['GET'])
def get_user_bookings(user_id):
    bookings = ClassroomUsage.query.filter_by(occupier_id=user_id).all()
    return jsonify([{
        'classroom_id': b.classroom_id,
        'start_time': b.start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': b.end_time.strftime('%Y-%m-%d %H:%M:%S')
    } for b in bookings])


# 教室信息查看
@app.route('/classrooms/info', methods=['GET'])
def get_classroom_info():
    location = request.args.get('location')
    classrooms = Classroom.query.filter(Classroom.location.contains(location)).all()
    return jsonify([{'id': c.id, 'type': c.type, 'capacity': c.capacity} for c in classrooms])


# 空闲教室查询
@app.route('/classrooms/available', methods=['GET'])
def get_available_classrooms():
    location = request.args.get('location')
    users = request.args.get('users', type=int)
    date = request.args.get('date')
    classroom_id = request.args.get('classroom_id')

    query = Classroom.query.filter(Classroom.location.contains(location))
    if users:
        query = query.filter(Classroom.capacity >= users)
    if classroom_id:
        query = query.filter_by(id=classroom_id)

    classrooms = query.all()
    available_classrooms = []

    for classroom in classrooms:
        usages = ClassroomUsage.query.filter_by(classroom_id=classroom.id).filter(
            ClassroomUsage.start_time >= date + ' 00:00:00',
            ClassroomUsage.end_time <= date + ' 23:59:59'
        ).all()

        occupied_times = [(u.start_time, u.end_time) for u in usages]
        available_times = calculate_available_times(occupied_times, date)

        for available in available_times:
            available_classrooms.append({
                'id': classroom.id,
                'location': classroom.location,
                'available_time': available
            })

    return jsonify(available_classrooms)


def calculate_available_times(occupied_times, date):
    start_of_day = datetime.strptime(date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
    end_of_day = datetime.strptime(date + ' 23:59:59', '%Y-%m-%d %H:%M:%S')

    available_times = []
    current_time = start_of_day

    for start, end in sorted(occupied_times):
        if current_time < start:
            available_times.append({
                'start': current_time.strftime('%Y-%m-%d %H:%M:%S'),
                'end': start.strftime('%Y-%m-%d %H:%M:%S')
            })
        current_time = max(current_time, end)

    if current_time < end_of_day:
        available_times.append({
            'start': current_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end': end_of_day.strftime('%Y-%m-%d %H:%M:%S')
        })

    return available_times