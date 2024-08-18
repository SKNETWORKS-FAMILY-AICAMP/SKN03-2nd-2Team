import { createRouter, createWebHistory } from 'vue-router'
import MoonvieHome from '@/views/MoonvieHome.vue'
import MoonvieMonth from '@/views/MoonvieMonth.vue'
import MoonviePeriod from '@/views/MoonviePeriod.vue'
import MoonvieGenre from '@/views/MoonvieGenre.vue'

const routes = [
  { path: '/', component: MoonvieHome },
  { path: '/month', component: MoonvieMonth },
  { path: '/period', component: MoonviePeriod },
  { path: '/genre', component: MoonvieGenre }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
