<template>
  <navbar-component-vue @getSearchText="search"/>
  <selectbar-component-vue @getCategoryId="categoryId"/>
  
  <div class="mb-3" v-if="searchTextRule">
    <h3>Productos con el texto <strong>{{ searchTextRule }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los Productos</button>
    <div class="alert alert-warning mt-3" role="alert" v-if="filteredProducts.length === 0" >No existen productos con el texto <strong>{{ searchTextRule }}</strong>
    </div>
  </div>



  <div class="mb-3" v-if="categoryReceived">
    <h4>Productos de la categoria <strong>{{categoryReceived}}</strong></h4>
    <button class="btn btn-dark" @click="resetFilter">Mostrar Todas las categorias</button>
  </div>
  <div class="alert alert-warning mt-3" role="alert" v-if="filteredProducts.length===0">
    No hay productos en la categoria {{categoryReceived}}!
  </div>

  <div class="container">
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div class="col" v-for="product in filteredProducts" :key="product.id">
      <!-- INICIO TARJETA -->
      <div class="card" style="width: 18rem;">
        <img :src="product.image" class="card-img-top" alt="imagen de {{product.name}}">
        <div class="card-body">
          <h5 class="card-title">{{product.name}}</h5>
          <h6 class="card-subtitle mb-2 text-body-secondary">{{product.category_name}}</h6>
          <p class="card-text">{{product.description}}</p>
          <a href="#" class="btn btn-primary">Comprar</a>
        </div>
        <div class="card-footer text-danger">
          <p>PRECIO: $ {{product.price}} - por ({{product.price_type_description}})</p>
        </div>
      </div>
      <!-- FIN TARJETA -->
      </div>
      </div>
  </div>

  
</template>

<script setup>
  import axios from 'axios'
  import SelectbarComponentVue from "@/components/SelectbarComponent.vue"
  import NavbarComponentVue from '@/components/NavbarComponent.vue'
  import {ref, onMounted} from 'vue'
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'
    
  const products = ref([])
  const filteredProducts=ref([])
  const categoryReceived=ref(null)
  const searchTextRule = ref(null)

  const search = (searchText) => {
    categoryReceived.value = null
    searchTextRule.value = searchText

    if (searchText) {
      filteredProducts.value = products.value.filter((product) => {
        const productName = product.name.toLowerCase();
        const productDescription = product.description.toLowerCase();
        const searchTerm = searchText.toLowerCase();

        return (
          productName.includes(searchTerm) || productDescription.includes(searchTerm)
        )
      })
    } else {
      filteredProducts.value = products.value
    }
  }  
  
  const categoryId = (categoryId, categoryName) => {
    searchTextRule.value = null
    categoryReceived.value = categoryName
    if (categoryId){
      filteredProducts.value=products.value.filter((product) => product.category === categoryId)
      } else {
        filteredProducts.value=products.value
      }
    }
  const resetFilter = () => {
      categoryReceived.value = null
      searchTextRule.value = null
      filteredProducts.value = products.value  
    }
  
  onMounted(()  => {
    axios.get("http://localhost:8000/api/products/")
    .then(response =>{
      products.value=response.data
      filteredProducts.value=products.value
    })
    .catch(error =>{
      console.log(error)
    })  
  })
  
</script>

<style>
  
</style>