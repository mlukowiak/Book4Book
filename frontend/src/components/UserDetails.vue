<template>
<div class="row">​
    Test
    {{userDetails.username}}
</div>   
</template>



<script>

import axios from 'axios';

export default {
  name: 'UserDetails',
  components: {
  },
  props: {
    id: {
      required: true,
      type: String,
    },
  },
data() {
      return {
          userDetails: Object,
      }
      },
  methods: {
      getDetails() {
          axios.get("http://127.0.0.1:8000/api/v1/users/" + this.id)
          .then(res => (this.userDetails = res.data))
          .catch(err => console.log(err));
      }
      },
  created() {
      this.getDetails()
      }
}
</script>
