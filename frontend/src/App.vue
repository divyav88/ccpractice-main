<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
/* eslint-disable */
import Home from "./components/Home.vue";
import Navbar from "./components/Navigation";


export default {
  name: "App",
  props: ["keycloak"],
  components: {
    Home,
    Navbar
  },
  // data() {
    
  // },
  mounted() {
  
  }
};
</script>
