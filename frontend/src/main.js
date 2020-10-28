import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue} from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import moment from 'moment';

Vue.filter('formatDate', function(value) {
  if (value) {
      return moment(String(value)).format('DD.MM.YYYY hh:mm')
  }
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
