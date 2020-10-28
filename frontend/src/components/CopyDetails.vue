<template>
<div class="row">​
    Test
    {{copyDetails.title}}
</div>   
</template>



<script>

import axios from 'axios';

export default {
  name: 'CopyDetails',
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
          copyDetails: Object,
      }
      },
  methods: {
      getDetails() {
          axios.get("http://127.0.0.1:8000/api/v1/copies/" + this.id)
          .then(res => (this.copyDetails = res.data))
          .catch(err => console.log(err));
      }
      },
  created() {
      this.getDetails()
      }
}
</script>
