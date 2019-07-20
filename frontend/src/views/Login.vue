<template>
  <div class="row">
    <div class="col-lg-4 offset-lg-4 col-md-6 offset-md-3 col-sm-10 offset-sm-1 col-12 offset-0">
      <form class="form login" @submit.prevent="login">
        <div class="form-row">
          <div class="form-group col-md-4 offset-md-4">
            <h2>LOGIN</h2>
          </div>
          <div class="form-group col-md-3 offset-md-1" v-show="loading">
            <loading-icon></loading-icon>
          </div>
        </div>
        <div class="form-group">
          <input required type="text" class="form-control" id="username" v-model="username" placeholder="Your group's name">
        </div>
        <div class="form-group">
          <input type="password" class="form-control" id="password" v-model="password" placeholder="Password">
        </div>
        <button type="submit" class="btn btn-primary">SUBMIT</button>
        <message-box class="error" messageType="error" v-if="error">{{ errorMsg }}</message-box>
        <footer>Don't have a password?<br> Raise your hand and wait for an instructor</footer>
      </form>

    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import LoadingIcon from '@/components/LoadingIcon.vue'
import MessageBox from '@/components/MessageBox.vue'

@Component({components: {LoadingIcon, MessageBox}})
export default class Login extends Vue {
  private username: string = ''
  private password: string = ''
  private loading = false
  private error = false
  private errorMsg: string = ''

  private login() {
    this.loading = true
    this.$store.dispatch('user/login', {username: this.username, password: this.password})
    .then((resp) => {
      this.loading = false
      this.error = false
      this.$store.dispatch('fetchBaseState')
      this.$router.push({name: 'home'})
    })
    .catch((err) => {
      this.loading = false
      this.error = true
      this.errorMsg = err.response.data.detail
    })
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/_variables.scss';

h2 {
  color: $brand-blue;
}

#username {
  margin-top: 30px;
}

form {
  background-color: rgb(255, 255, 255);
  padding: 20px;
  color: black;
  min-height: 300px;
}

.form-row {
  height: 40px;
}

form input {
  border-radius: 0px;
}

form input::placeholder {
  font-weight: bold;
}

form button {
  width: 100%;
  border-radius: 0px;
  font-weight: bold;
  background-color: $brand-teal;
  border-color: lighten($brand-teal, 5%);
}

form button:hover {
  background-color: lighten($brand-teal, 10%);
  border-color: lighten($brand-teal, 15%);
}

footer {
  margin-left: 15px;
  margin-right: 15px;
  margin-top: 0.8vw;
  margin-bottom: -10px;
  padding-bottom: 0px;
  font-size: 14px;
  color: grey;
}

.error {
  margin-top: 20px;
}
</style>

