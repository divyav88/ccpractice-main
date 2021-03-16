/* eslint-disable */
import Vue from 'vue';
import Router from 'vue-router';
import Requests from '../components/Requests.vue';
import Ping from '../components/Ping.vue';
import Home from '../components/Home.vue';


import * as Keycloak from 'keycloak-js';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/dashboard',
      name: 'Requests',
      component: Requests,
      // meta: {
      //   requiresAuth: true,
      // },
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
  ],
});



router.beforeEach((to, from, next) => {
 console.log(to);
 if(to.matched.some(record => record.meta.requiresAuth)) {
     
  const initOptions = {
    url: 'https://iam.aot-technologies.com/auth', realm: 'foirealm', clientId: 'foiclientfe', onLoad: 'login-required',
  };
  const keycloak = Keycloak(initOptions);

    keycloak.init({ onLoad: initOptions.onLoad }).then((auth) => {
      console.log(auth);
      if (!auth) {
        window.location.reload();
      } else {
        Vue.$log.info('Authenticated'); 
        var userprofile =  keycloak.loadUserProfile().then(p=>{
          console.log(p.username);
          console.log(p.email);
        })
       
        localStorage.setItem("vue-token", keycloak.token);
        localStorage.setItem("vue-refresh-token", keycloak.refreshToken);
        next();
    }

    //Token Refresh
      setInterval(() => {
        keycloak.updateToken(70).then((refreshed) => {
          if (refreshed) {
            Vue.$log.info('Token refreshed' + refreshed);
          } else {
            Vue.$log.warn('Token not refreshed, valid for '
              + Math.round(keycloak.tokenParsed.exp + keycloak.timeSkew - new Date().getTime() / 1000) + ' seconds');
          }
        }).catch(() => {
          Vue.$log.error('Failed to refresh token');
        });
      }, 6000);

    }).catch(() => {
      Vue.$log.error('Authenticated Failed');
    });

 }
 else{
   next();
 } 
})

export default router