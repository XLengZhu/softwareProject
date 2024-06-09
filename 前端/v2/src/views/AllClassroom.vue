<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { ElMessage } from 'element-plus';
    import { User, Lock } from '@element-plus/icons-vue';
    import {userAllClassroomService} from '@/api/user.js'
    const getit = async () => {
    //registerData是一个响应式对象,如果要获取值,需要.value
    let result = await userAllClassroomService();
    ElMessage.success(result.msg ? result.msg : '获取可用教室成功')
    Classroom.value = result
}
    const Classroom = ref({
        id: '',
        location: '',
        capacity: '',
        type: ''
    });
</script>

<template>
    <div>
        <h1>教室</h1>
        <h2>classroom</h2>
        <button @click="getit">获取</button>
        <table>
            <tr>
                <th>id</th>
                <th>location</th>
                <th>capacity</th>
                <th>type</th>
            </tr>
            <tr v-for="classroom in Classroom">
                <td>{{classroom.id}}</td>
                <td>{{classroom.location}}</td>
                <td>{{classroom.capacity}}</td>
                <td>{{classroom.type}}</td>
            </tr>
        </table>
    </div>
</template>

<!-- <template>
    <el-table
      :data="tableData"
      border
      style="width: 100%">
      <el-table-column
        prop="date"
        label="教室号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="地点"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="容量">
      </el-table-column>
      <el-table-column
        prop="type"
        label="类型">
      </el-table-column>
    </el-table>
  </template>
  
  <script>
    export default {
      data() {
        return {
          tableData: [{
            date: 'C101',
            name: 'Building 1',
            address: '30',
            type:'ordinary'
          }, {
            date: 'C101',
            name: 'Building 1',
            address: '30',
            type:'ordinary'
          }, {
            date: 'C101',
            name: 'Building 1',
            address: '30',
            type:'ordinary'
          }, {
            date: 'C101',
            name: 'Building 1',
            address: '30',
            type:'ordinary'
          }, ]
        }
      }
    }
  </script> -->