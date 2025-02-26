import { createApp } from 'vue'
import App from './App.vue'
import Router from './Router'

import './assets/main.css'

const app = createApp(App);
app.use(Router);
app.mount('#app');