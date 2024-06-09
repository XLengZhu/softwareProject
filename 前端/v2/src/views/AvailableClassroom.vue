<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { ElMessage } from 'element-plus';
    import {userAvaiClassroomService} from '@/api/user.js'
    const getAvailable = async () => {
        let result = await userAvaiClassroomService(restriction.value);
        ElMessage.success(result.msg ? result.msg : '查询成功')
        recieveFromServer.value = result
    }
    const restriction = ref({
        location: '',
        users:'',
        date: '',
        classroom_id:''
    });
    const recieveFromServer = ref({
        id: '',
        location: '',
        available_time: ''
    });
    const tempDate = ref({
        year: '',
        month: '',
        day: ''
    });

    </script>

<template>
    <div>
        <h1>查询指定地点的教室可用时间</h1>
        <h2>restriction</h2>
        location: <input type="text" v-model="restriction.location">
        <br>
        users:<input type="text" v-model="restriction.users">
        <br>    
        year-month-day: <input type="text" v-model="restriction.date">
        <br>
        classroom_id: <input type="text" v-model="restriction.classroom_id">
        
        <button @click="getAvailable">查询</button>
        <br>
        <table>
            <tr>
                <th>id</th>
                <th>location</th>
                <th>available_time</th>
            </tr>
            <tr v-for="reci in recieveFromServer">
                <td>{{reci.id}}</td>
                <td>{{reci.location}}</td>
                <td>{{reci.available_time}}</td>
            </tr>
        </table>
    </div>
</template>