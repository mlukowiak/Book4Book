<template>
  <div>
      <Header/>
      <AddCopy/>
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import AddCopy from '../components/AddCopy.vue'

export default {
    name: 'AddCopyPage',
    components: {
      Header,
      AddCopy
  }
}
</script>
