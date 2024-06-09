<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { ElMessage } from 'element-plus';
    import {adminChangeLevelService} from '@/api/admin.js';
    const changeLevel = async () => {
        let result = await adminChangeLevelService(userToBeChanged.value, permissionToBeChanged.value);
        if(result.code==200){
            ElMessage.success('修改权限成功')
        }
        else{
            ElMessage.error('修改权限失败')
        }
        recieveFromServer.value = result
    }
    const userToBeChanged = ref({
        id: ''
    });
    const permissionToBeChanged = ref({
        permission: true
    });
    const recieveFromServer = ref({});

</script>

<template>
    <h1>修改用户权限</h1>
    <h2>user</h2>
    id: <input type="text" v-model="userToBeChanged.id">
    <br>
    <button @click="changeLevel">修改</button>
    <br>

</template>