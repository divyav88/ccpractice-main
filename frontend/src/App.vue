<template>
  <div id="app">
     <Navbar/>
    <router-view />
    <!-- <h1>HELLO</h1>
     <h2 style="margin-left: 50px;">User: {{keycloak.tokenParsed.preferred_username}}</h2> -->
  </div>
</template>

<script>
import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>