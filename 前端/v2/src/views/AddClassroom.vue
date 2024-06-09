<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import {adminAddClassroomService} from '@/api/admin.js'
    import { ElMessage } from 'element-plus';
    const addClassroom = async () => {
        let result = await adminAddClassroomService(ClassroomToBeAdd.value);
        ElMessage.success(result.msg ? result.msg : '增加教室成功')
        recieveFromServer.value = result
    }
    const ClassroomToBeAdd = ref({
        id: '',
        location: '',
        capacity: '',
        type: ''
    });
    const recieveFromServer = ref({});

    

</script>


<template>
    <h1>添加教室</h1>
    <h2>classroom</h2>
    id: <input type="text" v-model="ClassroomToBeAdd.id">
    <br>
    location: <input type="text" v-model="ClassroomToBeAdd.location">
    <br>
    capacity: <input type="text" v-model="ClassroomToBeAdd.capacity">
    <br>
    type: <input type="text" v-model="ClassroomToBeAdd.type">
    <br>
    <button @click="addClassroom">添加</button>
    <br>
    <p>{{recieveFromServer.value}}</p>
    
</template>