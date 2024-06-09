<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import {userBookService} from '@/api/user.js'
    import { ElMessage } from 'element-plus';
    const getBooking = async () => {
        let result = await userBookService(BookingUser.value);
        ElMessage.success(result.msg ? result.msg : '预定教室查询成功')
        bookingMessage.value = result
    }
    const BookingUser = ref({
        id: '',
    });
    const bookingMessage = ref({
        classroom_id: '',
        start_time: '',
        end_time: ''
    });
</script>

<template>
    <div>
        <h1>查询用户预定</h1>
        <h2>booking</h2>
        id: <input type="text" v-model="BookingUser.id">
        <br>
        <button @click="getBooking">查询</button>
        <br>
        <table>
            <tr>
                <th>classroom id</th>
                <th>start time</th>
                <th>end time</th>
            </tr>
            <tr v-for="booking in bookingMessage">
                <td>{{booking.classroom_id}}</td>
                <td>{{booking.start_time}}</td>
                <td>{{booking.end_time}}</td>
            </tr>
        </table>
    </div>
</template>