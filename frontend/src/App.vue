<template>
  <div id="app">
    <navbar></navbar>
    <div class="container-fluid">
      <router-view/>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Navbar from '@/components/Navbar.vue'
import store from '@/store'
import router from '@/router'
import { AxiosError } from 'axios'

@Component({components: { Navbar }})
export default class App extends Vue {
  // Add hook to redirect to login page if received 401 (unauthorized)
  private beforeCreate() {
    this.$http.interceptors.response.use((response) => response, (err: AxiosError<any>) => {
      if (err.response && err.response.status === 401) {
        store.dispatch('logout')
        router.push('login')
      }
      return Promise.reject(err)
    })
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/_variables.scss';
@import '@/assets/styles/font-registration.scss';

#app {
  font-family: 'Proxima Nova';
  font-weight: 600;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  font-size: 16pt;

  background: url('~@/assets/img/bg-pattern.png'), $bg-color;
  background: url('~@/assets/img/bg-pattern.png'), -webkit-linear-gradient(to left, $bg-color, $bg-color-dark);
  background: url('~@/assets/img/bg-pattern.png'), linear-gradient(to left, $bg-color, $bg-color-dark);

  min-height: 100vh;
  padding-bottom: 20px;
}
</style>
