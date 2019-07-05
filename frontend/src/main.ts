import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import store from './store'
import Axios, { AxiosStatic } from 'axios'


Vue.config.productionTip = false
Vue.prototype.$http = Axios
Vue.prototype.$http.defaults.withCredentials = true  // Includes cookies in requests
declare module 'vue/types/vue' {
  interface Vue {
    $http: AxiosStatic
  }
}

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
