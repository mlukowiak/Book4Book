import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import CopyDetails from '@/components/CopyDetails.vue'

Vue.use(Router)


export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/copy/:id',
      name: 'copy',
      component: CopyDetails,
      props: true,
    },
  ],
});