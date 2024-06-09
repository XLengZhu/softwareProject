<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import {adminDeleteClassroomService} from '@/api/admin.js'
    import { ElMessage } from 'element-plus';
    const deleteClassroom = async () => {
    let result = await adminDeleteClassroomService(ClassroomToBeDeleted.value);
    ElMessage.success(result.msg ? result.msg : '删除教室成功')
    recieveFromServer.value = result
}
    const ClassroomToBeDeleted = ref({
        id: ''
    });
    const recieveFromServer = ref({});

    
</script>


<template>
    <h1>删除教室</h1>
    <h2>classroom</h2>
    id: <input type="text" v-model="ClassroomToBeDeleted.id">
    <br>
    <button @click="deleteClassroom">删除</button>
    <br>
    <p>{{recieveFromServer.value}}</p>
</template>