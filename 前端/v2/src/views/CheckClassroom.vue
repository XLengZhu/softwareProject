<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { ElMessage } from 'element-plus';
    import {userCheckService} from '@/api/user.js';
    const getClassroom = async () => {
        let result = await userCheckService(Classroom.value);
        ElMessage.success(result.msg ? result.msg : '查询成功')
        recieveFromServer.value = result
    }
    const Classroom = ref({
        location: ''
    });
    const recieveFromServer = ref({
        id: '',
        type: '',
        capacity: ''
    });

</script>

<template>
    <div>
        <h1>查询指定地点的教室信息</h1>
        <h2>classroom</h2>
        location: <input type="text" v-model="Classroom.location">
        <br>
        <button @click="getClassroom">查询</button>
        <br>
        <table>
            <tr>
                <th>id</th>
                <th>type</th>
                <th>capacity</th>
            </tr>
            <tr v-for="reci in recieveFromServer">
                <td>{{reci.id}}</td>
                <td>{{reci.type}}</td>
                <td>{{reci.capacity}}</td>
            </tr>
        </table>
    </div>
</template>