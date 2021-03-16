/* eslint-disable */
import * as Keycloak from 'keycloak-js';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import VueLogger from 'vuejs-logger';

Vue.use(BootstrapVue);
Vue.use(VueLogger);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');

// const initOptions = {
//   url: 'https://iam.aot-technologies.com/auth', realm: 'foirealm', clientId: 'foiclientfe', onLoad: 'login-required',
// };

// const keycloak = Keycloak(initOptions);

// keycloak.init({ onLoad: initOptions.onLoad }).then((auth) => {
//   if (!auth) {
//      window.location.reload();
//   } else {
//     Vue.$log.info('Authenticated');
//     new Vue({ router,   
//       render: h => h(App, { props: { keycloak: keycloak } }),     
//     }).$mount('#app')
//     localStorage.setItem("vue-token", keycloak.token);
//     localStorage.setItem("vue-refresh-token", keycloak.refreshToken);
//   }

// //Token Refresh
//   setInterval(() => {
//     keycloak.updateToken(70).then((refreshed) => {
//       if (refreshed) {
//         Vue.$log.info('Token refreshed' + refreshed);
//       } else {
//         Vue.$log.warn('Token not refreshed, valid for '
//           + Math.round(keycloak.tokenParsed.exp + keycloak.timeSkew - new Date().getTime() / 1000) + ' seconds');
//       }
//     }).catch(() => {
//       Vue.$log.error('Failed to refresh token');
//     });
//   }, 6000);

// }).catch(() => {
//   Vue.$log.error('Authenticated Failed');
// });
