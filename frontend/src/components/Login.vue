<template>
    <b-nav-item @click="login">Login</b-nav-item>
</template>

<script>
import KeyCloakService from '../services/authentication';

export default {
  name: 'Login',
  // props: ['keycloak'],
  data() {
    return {
      user: this.user,
    };
  },
  methods: {
    async login() {
      await KeyCloakService();
      // if(localStorage.getItem('isAuthenticated')){
      //   console.log('Authenticated is true')
      //   debugger;
      //   router.push('/dashboard')
      // }
      console.log('Logged');
    },
  },
};
</script>
