<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { ElMessage } from 'element-plus';
    import {adminChangeClassroomService} from '@/api/admin.js';
    const getClassroom = async () => {
        let result = await adminChangeClassroomService(changeClassroom.value);
        ElMessage.success(result.msg ? result.msg : '修改教室状态成功')
        recieveFromServer.value = result
    }
    const changeClassroom = ref({
        classroom_id: '',
        start_time: '',
        end_time: '',
        occupier_id: ''
    });
    const recieveFromServer = ref({}); 
</script>

<template>
    <div>
        <h1>教室</h1>
        <h2>classroom</h2>
        classroom_id: <input type="text" v-model="changeClassroom.classroom_id">
        <br>
        start_time: <input type="text" v-model="changeClassroom.start_time">
        <br>
        end_time: <input type="text" v-model="changeClassroom.end_time">
        <br>
        occupier_id: <input type="text" v-model="changeClassroom.occupier_id">
        <br>
        <button @click="getClassroom">使用</button>
        <br>
        <p>{{recieveFromServer.value}}</p>
    </div>
</template>