import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserPost from '@/components/UserPost.vue'
import UserProfile from '@/components/UserProfile.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 루트경로 5173으로 들어오면 HomeView 컴포넌트가 보여진다.
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      // vue에서 Dynamic Route Matching => :변수명 (v-bind와 유사)
      path:'/user/:id',
      // name: 'user',
      component: UserView,
      children:[
        { path: '', name: 'user', componenet: UserProfile},
        { path: 'profile', name: 'user-profile', componenet: UserProfile},
        { path: 'posts', name: 'user-post', componenet: UserPost},
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        console.log(to, from)
        // 이미 로그인 되어 있는 상태면 원래 위치로 돌아가게 해버리기
        const isLoggined = true
        if (isLoggined) {
          // return false
          return { name: 'home' }
        }
      }
    }
  ],
})
// router.beforeEach((to, from)=>{
//   // 막아보기
//   const isLoggined = false
  
//   // 로그인이 아닌 페이지로 이동하려 할 때 로그인 아니면 로그인 페이지로 리다이렉트
//   if (!isLoggined && to.name !== 'login') {
//     alert('로그인 먼저')
//     return { name: 'login' }
//   }
//   // console.log(to, from)
//   // alert()
// })
export default router
