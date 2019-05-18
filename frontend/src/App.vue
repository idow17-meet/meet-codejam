<template>
  <div id="app">
    <navbar></navbar>
    <div class="container-fluid">
      <img src="./assets/logo.png">
      <p>lol</p>
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
@import '~@/assets/styles/font-registration.scss';

#app {
  font-family: 'Proxima Nova';
  font-weight: 600;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
