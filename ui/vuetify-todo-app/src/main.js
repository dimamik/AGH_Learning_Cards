import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from "axios";
import AuthService from "./services/AuthService";

Vue.config.productionTip = false;

axios.defaults.baseURL = "http://localhost:5000";
axios.defaults.headers["Content-Type"] = "application/json";
//axios.defaults.headers["Access-Control-Allow-Origin"] = '*';
axios.defaults.withCredentials = true

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')

AuthService.loadCurrent();
