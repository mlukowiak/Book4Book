<template>
<div class="text-center">
  <form class="form-signin" @submit.prevent="login">
      <h1 class="h3 mb-3 font-weight-normal">Zaloguj się</h1>
      <label for="inputUsername" class="sr-only">Username</label>
      <input type="username" id="inputUsername" class="form-control" placeholder="Username" required autofocus v-model="username">
      <label for="inputPassword" class="sr-only">Hasło</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Hasło" required v-model="password">
      <button class="btn btn-lg btn-primary btn-block" type="submit">Zaloguj</button>
      <p class="mt-5 mb-3 text-muted">&copy; 2020 Book4Book</p>
    </form>
    </div>
</template>

<style scoped>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
</style>

<script>

import axios from 'axios';

export default {
  name: 'LoginForm',
  components: {

  },
  data(){
      return{
          username: '',
          password: '',
          token: localStorage.getItem('user-token') || null,
      }
  },
  methods: {
      login(){
          axios.post('http://127.0.0.1:8000/auth/',{
              username: this.username,
              password: this.password,
          })
          .then(resp => {
              this.token = resp.data.token;
              localStorage.setItem('user-token', resp.data.token)
              this.$router.push(this.$route.query.redirect || '/')
              })
          .catch(err => {
              localStorage.removeItem('user-token')
          })
      }
  }
}
</script>
