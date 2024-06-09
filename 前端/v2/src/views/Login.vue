<script setup>
import { User, Lock } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { ElMessage } from 'element-plus';
import {useRouter} from 'vue-router';
    const router = useRouter();
    const registerForm = ref({
        id: '',
        name: '',
        password: '',
        repassword: '',
        permisson: true
    });
    
    import {userRegisterService, userLoginService} from '@/api/user.js';
    const register = async () => {
    //registerData是一个响应式对象,如果要获取值,需要.value
    let result = await userRegisterService(registerForm.value);
    if(result.code!=201){
        ElMessage.error(result.msg ? result.msg : '注册失败')
    }
    else{
    ElMessage.success(result.msg ? result.msg : '注册成功')
    router.push('/layout')
    }
}
    const login= async () => {
        //registerData是一个响应式对象,如果要获取值,需要.value
        let result = await userLoginService(Login.value);
        if(result.code!=200){
        ElMessage.error(result.msg ? result.msg : '登录失败')
        }
        else{
        ElMessage.success(result.msg ? result.msg : '登录成功')
        router.push('/layout')
        }
    }
    const Login = ref({
        id: '',
        password: ''
    })
//控制注册与登录表单的显示， 默认显示注册
    const isRegister = ref(false)
     const checkRePassword = (rule, value, callback) => {
        if (value === '') {
            callback(new Error('请再次输入密码'))
        } else if (value !== registerForm.value.password) {
            callback(new Error('两次输入密码不一致'))
        } else {
            callback()
        }
    }
//define the rules of the form
const rules = ref({
    id: [
        { required: true, message: '请输入账号ID', trigger: 'blur' },
        { min: 5, max: 16, message: '长度在 5 到 16 个字符', trigger: 'blur'}    
    ],
    name: [
        { required: true, message: '请输入昵称', trigger: 'blur' },
        { min: 5, max: 16, message: '长度在 5 到 16 个字符', trigger: 'blur'}
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 5, max: 16, message: '长度在 5 到 16 个字符', trigger: 'blur'}
    ],
    repassword: [
        {validator: checkRePassword, trigger: 'blur'}
    ],
})

</script>

<template>
    <el-row class="login-page">
        <el-col :span="12" class="bg"></el-col>
        <el-col :span="6" :offset="3" class="form">
            <!-- 注册表单 -->
            <el-form ref="form" size="large" autocomplete="off" v-if="isRegister" :model="registerForm" :rules="rules">
                <el-form-item>
                    <h1>注册</h1>
                </el-form-item>
                <el-form-item prop="name">
                    <el-input :prefix-icon="User" v-model="registerForm.name" placeholder="请输入昵称"></el-input>
                </el-form-item>
                <el-form-item prop="id">
                    <el-input :prefix-icon="User" v-model="registerForm.id" placeholder="请输入账号ID"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input :prefix-icon="Lock" v-model="registerForm.password" type="password" placeholder="请输入密码" show-password></el-input>
                </el-form-item>
                <el-form-item prop="repassword">
                    <el-input :prefix-icon="Lock" v-model="registerForm.repassword" type="password" placeholder="请输入密码" show-password></el-input>
                </el-form-item>
                <!-- 注册按钮 -->
                <el-form-item>
                    <el-button class="button" type="primary" @click="register" auto-insert-space>
                        注册
                    </el-button>
                </el-form-item>
                <el-form-item class="flex">
                    <el-link type="info" :underline="false" @click="isRegister = false">
                        ← 返回
                    </el-link>
                </el-form-item>
            </el-form>
            <!-- 登录表单 -->
            <el-form ref="form" size="large" autocomplete="off" :model="Login" :rules="rules" v-else>
                <el-form-item>
                    <h1>登录</h1>
                </el-form-item>
                <el-form-item prop="id">
                    <el-input :prefix-icon="User" v-model="Login.id" placeholder="请输入账号ID" ></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input name="password" :prefix-icon="Lock" v-model="Login.password" type="password" placeholder="请输入密码" show-password></el-input>
                </el-form-item>
                <el-form-item class="flex">
                    <div class="flex">
                        <el-checkbox>记住我</el-checkbox>
                        <el-link type="primary" :underline="false">忘记密码？</el-link>
                    </div>
                </el-form-item>
                <!-- 登录按钮 -->
                <el-form-item>
                    <el-button class="button" type="primary" @click="login" auto-insert-space>登录</el-button>
                </el-form-item>
                <el-form-item class="flex">
                    <el-link type="info" :underline="false" @click="isRegister = true">
                        注册 →
                    </el-link>
                </el-form-item>
            </el-form>
        </el-col>
    </el-row>
    <router-link to="/login/admin">管理员登录/注册</router-link>
</template>

<style lang="scss" scoped>
/* 样式 */
.login-page {
    height: 100vh;
    background-color: #fff;

    .bg {
        background: url('@/assets/logo2.png') no-repeat 60% center / 240px auto,
            url('@/assets/login_bg.jpg') no-repeat center / cover;
        border-radius: 0 20px 20px 0;
    }

    .form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        user-select: none;

        .title {
            margin: 0 auto;
        }

        .button {
            width: 100%;
        }

        .flex {
            width: 100%;
            display: flex;
            justify-content: space-between;
        }
    }
}
</style>