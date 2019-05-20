<template>
  <div id="app">
    <navbar></navbar>
    <div class="container-fluid">
      <router-view/>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import Navbar from '@/components/Navbar.vue';

@Component({components: { Navbar }})
export default class App extends Vue {
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/_variables.scss";
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
