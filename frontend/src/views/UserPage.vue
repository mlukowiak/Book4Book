<template>
  <div>
    <Header/>
    <UserDetails :id="id"/>
  </div>
</template>

<script>

import Header from '../components/Header.vue'
import UserDetails from '../components/UserDetails'

export default {
  name: 'UserPage',
  props: ['id'],
  components: {
    Header,
    UserDetails,
  }
}
</script>
