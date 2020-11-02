<template>
  <div>
    <Header/>
    <CopyDetails :id="id"/>
  </div>
</template>

<script>

import Header from '../components/Header.vue'
import CopyDetails from '../components/CopyDetails.vue'

export default {
  name: 'CopyDetailsPage',
  props: ['id'],
  components: {
    Header,
    CopyDetails
  }
}
</script>
