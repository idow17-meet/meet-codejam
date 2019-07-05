<template>
  <div class="col-md-6 offset-md-3">
    <form class="form login" @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username</label>
        <input required type="text" class="form-control" id="username" v-model="username" placeholder="Your group's name">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" v-model="password" placeholder="Password">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <p v-if="error">Error: {{ errorMsg }}</p>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
export default class Login extends Vue {
  private username: string = ''
  private password: string = ''
  private loggingIn = false
  private error = false
  private errorMsg: string = ''

  private login() {
    this.loggingIn = true
    this.$store.dispatch('login', {username: this.username, password: this.password})
    .then((resp) => {
      this.loggingIn = false
      this.error = false
      this.$router.push('home')
    })
    .catch((err) => {
      this.loggingIn = false
      this.error = true
      this.errorMsg = err.response.data.detail
    })
  }
}
</script>

<style lang="scss" scoped>
</style>

