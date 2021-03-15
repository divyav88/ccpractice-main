<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="/">Logo</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav >
            <b-navbar-nav class="ml-auto">
                <!-- <b-nav-item href="/">Home</b-nav-item> -->
                <!-- <b-nav-item href="http://localhost:5000/dashboard">Login</b-nav-item> -->
                <Login/>
            </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
import Login from './Login.vue';

export default {
  name: 'Navbar',
  components: {
    Login,
  },
};
</script>
<style scoped>
.bg-info {
    background-color: #003366 !important;
}
</style>
