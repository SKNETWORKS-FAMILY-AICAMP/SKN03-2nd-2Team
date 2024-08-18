import { createRouter, createWebHistory } from 'vue-router'
<<<<<<< HEAD
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
=======

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:catchAll(.*)*',
      component: () => import('@/pages/ErrorNotFound.vue')
    },
    {
      path: '/',
      component: () => import('@/views/layouts/MainLayout.vue'),
      children: [
        /* index */
        {
          path: '/',
          component: () => import('@/views/HomeView.vue')
        },
        {
          path: '/top',
          component: () => import('@/views/TopMoviesView.vue')
        },
        {
          path: '/cloud',
          component: () => import('@/views/MovieCloudView.vue')
        },
        {
          path: '/genre',
          component: () => import('@/views/MovieGenreView.vue')
        },
        {
          path: '/season',
          component: () => import('@/views/MovieSeasonView.vue')
        },
        {
          path: '/region',
          component: () => import('@/views/MovieRegionView.vue')
        },
        {
          path: '/covid',
          component: () => import('@/views/MovieCovidView.vue')
        }
      ]
    }
  ]
>>>>>>> origin/hotfix
})

export default router
