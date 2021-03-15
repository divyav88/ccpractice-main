import * as Keycloak from 'keycloak-js';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import VueLogger from 'vuejs-logger';
import Vue from 'vue';
import router from '../router'

Vue.use(BootstrapVue);
Vue.use(VueLogger);

const KeyCloakService = () => {
  const initOptions = {
    url: 'https://iam.aot-technologies.com/auth', realm: 'foirealm', clientId: 'foiclientfe', onLoad: 'login-required',
  };
  const keycloak = Keycloak(initOptions);
   
  keycloak.init({ onLoad: initOptions.onLoad }).then((auth) => {
    if (!auth) {
      router.push('/')
    } else {  
      router.push('/dashboard')  
      localStorage.setItem('isAuthenticated',true)
      localStorage.setItem('vue-token', keycloak.token);
      localStorage.setItem('vue-refresh-token', keycloak.refreshToken);    
    } 
    // Token Refresh
    setInterval(() => {
      keycloak.updateToken(70).then((refreshed) => {
        if (refreshed) {
          Vue.$log.info(`Token refreshed${refreshed}`);
        } else {
          Vue.$log.warn(`Token not refreshed, valid for ${Math.round(keycloak.tokenParsed.exp + keycloak.timeSkew - new Date().getTime() / 1000)} seconds`);
        }
      }).catch(() => {
        Vue.$log.error('Failed to refresh token');
      });
    }, 100);
  }).catch(() => {
    Vue.$log.error('Authenticated Failed');
  });
};

export default KeyCloakService;
