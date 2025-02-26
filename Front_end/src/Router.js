import { createRouter, createWebHashHistory } from 'vue-router';
import Login from './components/Login.vue';
import Register from './components/Register.vue'

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/register', component: Register, alias: '/' },
        {path: '/login', component: Login}
    ]
})