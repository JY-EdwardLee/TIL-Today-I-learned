import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import Userview from '@/views/Userview.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user/:username',
      name: 'user',
      component: Userview
    }
  ]
})

router.beforeEach((to, from) => {
  console.log(to)
  console.log(from)
  if (to.name==='user' && to.params.username !=='admin') {
    alert('돌아가라')
    return {name:'home'}
  }
})


export default router
