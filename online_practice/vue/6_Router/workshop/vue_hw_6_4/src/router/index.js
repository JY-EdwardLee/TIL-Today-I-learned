import { createRouter, createWebHistory } from 'vue-router'
import StudentViews from '../views/StudentViews.vue'
import SomeView from '@/views/SomeView.vue'
import Otherview from '@/views/Otherview.vue'
import StudentDetailView from '../views/StudentDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/students/',
      name:'students',
      component: StudentViews,
    },
    {
      path:'/students/:name',
      name:'StudentDetail',
      component: StudentDetailView,
    },
    {
      path:'/',
      name:'some',
      component: SomeView,
    },
    {
      path:'/other',
      name:'other',
      component: Otherview,
    }
  ]
})

export default router
