<template>
	<section class="text-center mt-5 mx-auto">
    <!-- Titulo de la Pagina -->
    <h1>Panaderia y Pasteleria la 24</h1> 
    <!-- CARRUSEL -->
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
                aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
                aria-label="Slide 3"></button>
        </div>
        <!-- imagenes -->
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img :src="require('@/assets/img/pan1000x200_1.jpg')" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
                <img :src="require('@/assets/img/pan1000x200_2.jpg')" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
                <img :src="require('@/assets/img/pan1000x200_3.jpg')" class="d-block w-100" alt="...">
            </div>
        </div>
        <!-- controles -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
  <!-- FIN DEL CARROUSEL -->
  <!-- BARRA DE SELECCION DE CATEGORIAS -->
  <div class="mt-3" v-if="$route.path !== '/about'">
    <button class="btn btn-dark" v-for="category in categories" :key="category.id" @click="getCategory(category.id, category.name)">{{ category.name }}</button>
    <!--button class="btn btn-dark">Categoria 2</button>
    <button class="btn btn-dark">Categoria 3</button>
    <button class="btn btn-dark">Categoria 4</button-->
    <hr>
  </div>
  
  </section>
</template>

<script setup>
import axios from 'axios'
import {ref, defineEmits, onMounted} from 'vue'

const categories = ref([])
const categoryId = ref(null)
const categoryName = ref(null)
const emit = defineEmits(['getCategoryId'])

const getCategory = (id, name) => {
  emit('getCategoryId', id, name)
}

onMounted(() => {
  axios.get('http://127.0.0.1:8000/api/categories/')
  .then(response =>{
    categories.value= response.data
  })
  .catch(error => {
    console.log(error)
  })
})	
</script>

<style>
/* Estilos del componente */	
button {
  margin-right: 5px; 
}
button + button, button:first-child{
  margin-right:5px;
}
@media(max-width:768px){
  button {
    width: 100%;
    margin: 0 0 5px !important;
    box-sizing: border-box;
  }
}
</style>