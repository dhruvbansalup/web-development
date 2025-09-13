import { createWebHistory,createRouter } from "vue-router"
import Home from './components/home.vue'
import child from "./components/child.vue"

const routes=[
    {
        name:"Home",
        path:"/",
        component:Home,
    },
    {
        name:"Child",
        path:"/child",
        component:child
    }
]

const router=createRouter({
    history:createWebHistory(),
    routes
})

export default router;