<template>
  <div id="app">
    <navbar></navbar>
    <div class="container-fluid">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style lang="scss" scoped>
@import "~@/assets/styles/_variables.scss";
@import '~@/assets/styles/font-registration.scss';

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
