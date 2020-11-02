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
             <router-link :to="{ path: `/copy/${copy.id}`}">
             <img :src="copy.photo" class="card-img-top"/>
             </router-link>
            <div class="card-body">
                <router-link :to="{ path: `/copy/${copy.id}`}">
                    <h6 class="card-title">{{copy.title}}</h6>
                </router-link>
                <router-link :to="{ path: `/user/${copy.user.id}`}">
                    <p class="card-text">{{copy.user.username}}</p>
                </router-link>
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
.card-title {
    color: #6c757d;
    text-decoration: none;
}
.card-text {
    color: #6c757d;
    text-decoration: none;
}
</style>

<script>

import axios from 'axios';

export default {
  name: 'NewestCopies',
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
