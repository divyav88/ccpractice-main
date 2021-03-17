<template>
<div>
 <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="/">Logo</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav >
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="/">Home</b-nav-item>
      <b-nav-item href="/dashboard">Requests</b-nav-item>
        <b-nav-item href="/login">Login</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
/* eslint-disable */
    export default {
    name:'Navbar',
    // data(){
    //     return '';
    // }
}
</script>
<style scoped>
.bg-info {
    background-color: #003366 !important;
}
</style>