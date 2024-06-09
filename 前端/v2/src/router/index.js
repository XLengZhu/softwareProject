import { createRouter, createWebHistory } from 'vue-router'

//导入组件
import LoginVue from '@/views/Login.vue'
import AdminLoginVue from '@/views/AdminLogin.vue'
import LayoutVue from '@/views/Layout.vue'
import AdminLayoutVue from '@/views/AdminLayout.vue'
import availableClassroomsVue from '@/views/AvailableClassroom.vue'
import AllClassroomVue from '@/views/AllClassroom.vue'
import BookingsVue from '@/views/Bookings.vue'
import addClassroomVue from '@/views/AddClassroom.vue'
import DeleteClassroomVue from '@/views/DeleteClassroom.vue'
import ChangeClassroomVue from '@/views/ChangeClassroom.vue'
import CheckVue from '@/views/CheckClassroom.vue'
import ChangeVue from '@/views/ChangeLevel.vue'
// import ArticleCategoryVue from '@/views/article/ArticleCategory.vue'
// import ArticleManageVue from '@/views/article/ArticleManage.vue'
// import UserAvatarVue from '@/views/user/UserAvatar.vue'
// import UserInfoVue from '@/views/user/UserInfo.vue'
// import UserResetPasswordVue from '@/views/user/UserResetPassword.vue'

//定义路由关系
const routes = [
    { path: '/login/user', component: LoginVue},
    { path: '/login/admin', component: AdminLoginVue },
    {
        path: '/layout', component: LayoutVue,
        children:[
            {path: '/layout/availableClassrooms', component: availableClassroomsVue},
            {path: '/layout/allClassrooms', component: AllClassroomVue},
            {path: '/layout/check', component: CheckVue}
            
            // {path: '/layout/book', component: bookVue},
            // {path: '/layout/info', component: infoVue}
        ]
        // ,redirect:'/article/manage'
        // , children: [
        //     { path: '/article/category', component: ArticleCategoryVue },
        //     { path: '/article/manage', component: ArticleManageVue },
        //     { path: '/user/info', component: UserInfoVue },
        //     { path: '/user/avatar', component: UserAvatarVue },
        //     { path: '/user/resetPassword', component: UserResetPasswordVue }
        // ]
    },
    { path: '/adlayout', component: AdminLayoutVue,
        children:[
            {path: '/adlayout/add', component: addClassroomVue},
            {path: '/adlayout/delete', component: DeleteClassroomVue},
            {path: '/adlayout/change', component: ChangeClassroomVue},
            {path: '/adlayout/bookings', component: BookingsVue},
            {path: '/adlayout/changeLevel', component: ChangeVue}
        ]

     }

]

//创建路由器
const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

//导出路由
export default router
