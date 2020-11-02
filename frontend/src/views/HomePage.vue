<template>
  <div>
    <Header/>
    <MainSearch/>
    <NewestCopies/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import NewestCopies from '@/components/NewestCopies.vue'
import MainSearch from '@/components/MainSearch.vue'

export default {
  name: 'HomePage',
  components: {
    Header,
    NewestCopies,
    MainSearch
  }
}
</script>
