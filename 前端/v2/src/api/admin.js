//导入request.js请求工具
import request from '@/utils/request.js'

//提供调用注册接口的函数guanli
export const adminRegisterService = (registerData)=>{
    return request.post('/register/admin',registerData);
}

//提供调用登录接口的函数guanli
export const adminLoginService = (loginData)=>{
    return request.post('/login/admin',loginData)
}

export const adminAddClassroomService = (classroomData)=>{
    return request.post('/classrooms',classroomData)
}

export const adminDeleteClassroomService = (classroomData)=>{
    return request.delete('classrooms/'+classroomData['id'])
}

export const adminChangeClassroomService = (classroomData)=>{
    return request.post('classrooms/usage',classroomData)
}

export const adminChangeLevelService = (userData,permissionToBeChanged)=>{
    return request.put('users/'+userData['id']+'/permission',permissionToBeChanged)
}