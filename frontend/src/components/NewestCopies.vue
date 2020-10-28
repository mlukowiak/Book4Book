<template>
<div class="row">​
    <div class="col-md-6">
        <h6>Najnowsze ogłoszenia</h6>
    </div>
    <div class="col-md-6">
        <p class="text-right"><small>Zobacz wszystkie</small></p>
    </div>
    <div class="card-deck">
        <div class="card" v-bind:key="copy.id" v-for="copy in copies.slice(0, 5).reverse()">
            <img :src="copy.photo" class="card-img-top"/>
            <div class="card-body">
                <router-link :to="{ path: `/copy/${copy.id}`}">
                    <h6 class="card-title">{{copy.title}}</h6>
                </router-link>
                <p class="card-text">{{copy.user.username}}</p>
                <p class="card-text-bottom"><small class="text-muted">{{copy.date | formatDate}}</small></p>
            </div>
        </div>
    </div>
</div>   
</template>

<style scoped>
.card-img-top {
    height: 250px;
    object-fit: cover;
}
.card-text-bottom {
    position: absolute;
    bottom: 0;
}
</style>

<script>

import axios from 'axios';

export default {
  name: 'Home',
  components: {
      
  },
  data() {
      return {
          copies: [],
      }
      },
  methods: {
      getCopies() {
          axios.get("http://127.0.0.1:8000/api/v1/copies/")
          .then(res => (this.copies = res.data))
          .catch(err => console.log(err));
      }
      },
  created() {
      this.getCopies()
      }
}
</script>
