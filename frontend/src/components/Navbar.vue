<template>
  <nav class='navbar navbar-expand-lg navbar-dark container bg-dark navigation col-12'>
    <router-link class='navbar-brand' :to="{name: 'home'}" exact>meet codejam</router-link>
    <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarsExample09' aria-controls='navbarsExample09'
      aria-expanded='false' aria-label='Toggle navigation'>
      <span class='navbar-toggler-icon'></span>
    </button>

    <div class='collapse navbar-collapse' id='navbarsExample09'>
      <ul class='navbar-nav mr-auto'>
        <li class='nav-item'>
          <a class='nav-link' href='#broken'>leaderboard</a>
        </li>
          <li class='nav-item'>
            <router-link class='nav-link' :to="{name: 'home'}" exact>problems</router-link>
          </li>
          <li class='nav-item'>
            <a class='nav-link' href='#broken'>team</a>
          </li>
      </ul>
      <ul class='navbar-nav ml-auto'>
        <li class='nav-item'>
          <!-- {% if session['user_id'] %} -->
          <a class='nav-link' href='#broken'>sign out</a>
          <!-- {% else %}
          <a class='nav-link' href='#broken'>sign in</a>
          {%endif%} -->
        </li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
export default class Navbar extends Vue {
  public name = 'navbar'
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
