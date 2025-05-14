import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'

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
      paht:'/user/:id',
      name: 'user',
      componenet: UserView,
    }
  ],
})

export default router
