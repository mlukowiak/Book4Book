<template>
  <div>
    
    <AddCopy/>
    <Header/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import AddCopy from '@/components/AddCopy.vue'

export default {
    name: 'AddCopy',
    components: {
      Header,
      AddCopy
  }
}
</script>
