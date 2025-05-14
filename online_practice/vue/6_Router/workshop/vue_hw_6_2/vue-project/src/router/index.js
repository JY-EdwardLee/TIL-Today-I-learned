import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
import Otherview from '@/views/Otherview.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'some',
      component:SomeView,
    },
    {
      path:'/other',
      name:'other',
      component:Otherview,
    }
  ],
})

export default router
