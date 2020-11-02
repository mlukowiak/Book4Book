<template>
<div class="text-center">
  <form class="form-signin">
      <h1 class="h3 mb-3 font-weight-normal">Zaloguj się</h1>
      <label for="inputEmail" class="sr-only">Email</label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Email" required autofocus>
      <label for="inputPassword" class="sr-only">Hasło</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Hasło" required>
      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> Zapamiętaj mnie
        </label>
      </div>
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

export default {
  name: 'LoginForm',
  components: {

  }
}
</script>
