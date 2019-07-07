<template>
  <nav class='navbar navbar-expand-lg navbar-dark container bg-dark navigation col-12'>
    <router-link class='navbar-brand' :to="{name: 'home'}" exact>meet codejam</router-link>
    <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarsExample09' aria-controls='navbarsExample09'
      aria-expanded='false' aria-label='Toggle navigation'>
      <span class='navbar-toggler-icon'></span>
    </button>

    <div class='collapse navbar-collapse' id='navbarsExample09'>
      <ul class='navbar-nav mr-auto'>
        <template v-if="$store.getters['user/loggedIn']">
          <li class='nav-item'>
            <a class='nav-link' href='#broken'>leaderboard</a>
          </li>
          <li class='nav-item'>
            <router-link class='nav-link' :to="{name: 'home'}" exact>problems</router-link>
          </li>
          <li class='nav-item'>
            <router-link class='nav-link' :to="{name: 'groupProfile', params: {name: $store.getters['user/group'].name}}">team</router-link>
          </li>
        </template>
      </ul>
      <ul class='navbar-nav ml-auto'>
        <li class='nav-item'>
          <a v-if="$store.getters['user/loggedIn']" class='nav-link' href="#empty" @click.prevent.once="logout">sign out</a>
          <router-link v-else class='nav-link' :to="{name: 'login'}">login</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
export default class Navbar extends Vue {
  private logout() {
    this.$store.dispatch('logout')
    .then((response) => {
      this.$router.push({name: 'login'})
    })
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/_variables.scss";

.navbar {
  margin-bottom: 60px;
  font-family: 'ArcherPro';
  font-weight: bold;
}

a.navbar-brand, a.navbar-brand:focus{
  color: $brand-teal;
}
</style>
