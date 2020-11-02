<template>
<header class="blog-header py-3">
    <div class="row flex-nowrap justify-content-between align-items-center">
        <div class="col-4 pt-1">
            <h5 class="my-0 mr-md-auto font-weight-normal"> <router-link style="text-decoration: none; color: inherit"  :to="{ path: `/`}">Book4Book</router-link></h5>
        </div>
        <div class="col-4 d-flex justify-content-end align-items-center">
            <a class="btn btn-sm btn-outline-secondary"><router-link style="text-decoration: none; color: inherit" :to="{ path: `add`}">Wystaw książkę</router-link></a>
        </div>
    </div>
</header>
</template>

<style scoped>
.blog-header {
  border-bottom: 1px solid #e5e5e5;
}
router-link{
    text-decoration: none;
}
</style>

<script>

export default {
  name: 'Header',
  components: {
  }
}
</script>
