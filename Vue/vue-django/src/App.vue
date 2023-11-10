<template>
    <!----------  
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> 
    --> 
  <navbar-component-vue v-if="$route.path !='/'" />


  <selectbar-component-vue v-if="$route.path ==='/about'"/>
  <router-view/>

  <footer-component-vue/>

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script setup>
  import FooterComponentVue from "./components/FooterComponent.vue"
  import NavbarComponentVue from "./components/NavbarComponent.vue"
  import SelectbarComponentVue from "./components/SelectbarComponent.vue"
</script>
