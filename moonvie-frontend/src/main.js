<<<<<<< HEAD
=======
import './style.css'

>>>>>>> origin/hotfix
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
<<<<<<< HEAD

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

=======
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
>>>>>>> origin/hotfix
const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(createPinia()).use(router).use(pinia).mount('#app')
