import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '../views/HomePage.vue'
import LoginPage from '../views/LoginPage.vue'
import CopyDetails from '@/components/CopyDetails.vue'
import AddCopy from '@/components/AddCopy.vue'

Vue.use(Router)


export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: HomePage,
    },
    {
      path: '/login',
      component: LoginPage,
    },
    {
      path: '/copy/:id',
      name: 'copy',
      component: CopyDetails,
      props: true,
    },
    {
      path: '/add',
      name: 'add',
      component: AddCopy,
    },
  ],
});