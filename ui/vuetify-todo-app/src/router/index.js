import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CollectionsListComponent from "@/components/CollectionsListComponent";
import LearnCollection from "@/views/LearnCollection";
import Profile from "@/views/Profile";
import AuthComponent from "../components/auth/AuthComponent";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        alias: ['/home'],
        name: 'home',
        component: Home
    },
    {
        path: '/my-cards',
        name: 'my-cards',
        component: CollectionsListComponent
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile
    },
    {
        path: '/learn-collection',
        name: 'learn-collection',
        component: LearnCollection
    },
    {
        path: '/auth',
        name: 'auth',
        component: AuthComponent
    }
]

const router = new VueRouter({
    routes
})

export default router
