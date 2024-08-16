import { createRouter, createWebHistory } from 'vue-router';
import MoonvieHome from '@/views/MoonvieHome.vue';
import MoonvieMonth from '@/views/MoonvieMonth.vue';
import MoonviePeriod from '@/views/MoonviePeriod.vue';
import MoonvieGenre from '@/views/MoonvieGenre.vue';

const routes = [
  {
    path: '/',
    name: 'MoonvieHome',
    component: MoonvieHome
  },
  {
    path: '/month',
    name: 'MoonvieMonth',
    component: MoonvieMonth
  },
  {
    path: '/period',
    name: 'MoonviePeriod',
    component: MoonviePeriod
  },
  {
    path: '/genre',
    name: 'MoonvieGenre',
    component: MoonvieGenre
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
