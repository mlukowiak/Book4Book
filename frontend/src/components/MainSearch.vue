<template>
<div class="nav-scroller py-1 mb-2">
    <div class="nav d-flex justify-content-between">
        <input v-model="keywords" @input="getResults" class="form-control" type="text" placeholder="Szukaj książki" aria-label="Search">
        <div class="col-12" v-bind:key="result.id" v-for="result in results">
            <p>{{ result.title }} ({{ result.copies_number }})</p>
        </div>
    </div>
</div>
</template>

<style scoped>
.form-control {
    border: 0px;
    border-radius: 0px;
    height: 50px;
    text-align: center;
    font-size: x-large;
}
.form-control:hover {
  box-shadow: inset 0 -1px 0 0 #e5e5e5; 
  border-radius: 0px;
}

</style>

<script>

import axios from 'axios';

export default {
  name: 'MainSearch',
  components: {
  },
  data() {
      return {
          keywords: '',
          results: [],
      }
      },
  methods: {
      getResults() {
          if (this.keywords.length > 1){
              axios.get("http://127.0.0.1:8000/api/v1/books/?search="+this.keywords)
              .then(res => (this.results = res.data))
              .catch(err => console.log(err));
          }
      }
      },
      created() {
      this.getResults()
      }
}
</script>
