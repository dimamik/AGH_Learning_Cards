import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CollectionsListComponent from "@/components/CollectionsListComponent";
import LearnCollection from "@/views/LearnCollection";
import Profile from "@/views/Profile";

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
        alias: ['/my-cards'],
        name: 'my-cards',
        component: CollectionsListComponent
    },
    {
        path: '/profile',
        alias: ['/profile'],
        name: 'profile',
        component: Profile
    },
    {
        path: '/learn-collection',
        name: 'profile',
        component: LearnCollection
    }
]

const router = new VueRouter({
    routes
})

export default router
