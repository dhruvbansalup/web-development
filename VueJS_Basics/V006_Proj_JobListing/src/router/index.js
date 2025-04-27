import { createRouter, createWebHistory} from 'vue-router';
import HomeView from '@/views/homeView.vue'
import JobsView from '@/views/JobsView.vue';
import NotFound from '@/views/NotFound.vue';


const router=createRouter({
    history:createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path:'/',
            name:'home',
            component:HomeView
        },
        {
            path:'/jobs',
            name:'jobs',
            component:JobsView
        },
        {
            path:'/:catchAll(.*)*',
            name:'NotFound',
            component:NotFound
        },
    ],
});

export default router