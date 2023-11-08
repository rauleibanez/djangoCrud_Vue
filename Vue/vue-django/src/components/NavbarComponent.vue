<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <!--a class="nav-link active" aria-current="page" href="#">Home</a-->
        <router-link to="/" class="nav-link active">Inicio</router-link>
        <router-link to="/about" class="nav-link active">Acerca de...</router-link>        
      </div>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: 'NavbarComponent',
  /*components: {
    HelloWorld
  }*/
}	
</script>

<style>
	
</style>