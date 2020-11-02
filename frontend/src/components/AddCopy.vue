<template>
  <div>
      <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
          <li class="nav-item" role="presentation"><a class="nav-link active" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab" aria-controls="pills-home" aria-selected="true">Home</a></li>
          <li class="nav-item" role="presentation"><a class="nav-link" id="pills-profile-tab" data-toggle="pill" href="#pills-profile" role="tab" aria-controls="pills-profile" aria-selected="false">Profile</a></li>
    </ul>
    
<div class="tab-content" id="pills-tabContent">
  <div class="tab-pane fade show active" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">...</div>
  <div class="tab-pane fade" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab">...</div>
  <div class="tab-pane fade" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">...</div>
</div>

      <form id="formcopy">
          <input type="text" placeholder="Nazwa" name="title" id="title" v-model="title">
          <input type="textarea" placeholder="Opis" name="decription" id="decription" v-model="decription">

      </form>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'AddCopy',
  components: {

  }
}
</script>
