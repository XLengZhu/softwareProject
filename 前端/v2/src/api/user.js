//导入request.js请求工具
import request from '@/utils/request.js'

//提供调用注册接口的函数
export const userRegisterService = (registerData)=>{
    return request.post('/register/user',registerData);
}

//提供调用登录接口的函数
export const userLoginService = (loginData)=>{
    return request.post('/login/user',loginData)
}


//获取用户详细信息
export const userAllClassroomService = ()=>{
    return request.get('/classrooms')
}

export const userBookService = (bookData)=>{
    // const params = new URLSearchParams()
    // for(let key in bookData){
    //     params.append(key,bookData[key]);
    //     alert(params)
    // }
    return request.get('/user/'+bookData['id']+'/bookings')
}

export const userAvaiClassroomService = (filterData)=>{
    return request.get('/classrooms/available?location='+filterData.location+'&date='+filterData.date)
}

//修改个人信息
export const userInfoUpdateService = (userInfoData)=>{
   return request.put('/user/update',userInfoData)
}

//修改头像
export const userAvatarUpdateService = (avatarUrl)=>{
    const params = new URLSearchParams();
    params.append('avatarUrl',avatarUrl)
    return request.patch('/user/updateAvatar',params)
}

export const userCheckService = (locationData)=>{
    return request.get('/classrooms/info?location='+locationData.location)
}