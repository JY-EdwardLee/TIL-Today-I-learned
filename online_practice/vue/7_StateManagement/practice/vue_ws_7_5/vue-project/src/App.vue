<template>
<nav>
<RouterLink :to="{name: 'home'}" class="link">Home</RouterLink>
<RouterLink :to="{name: 'products'}" class="link">Products</RouterLink>
<RouterLink :to="{name: 'favorite'}" class="link" >
    Favorits
<span id="counter">{{counter}}</span>
</RouterLink>

</nav>
<div>
    <RouterView />
</div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import {useProductsStore} from '@/stores/products.js'
import {ref, computed} from 'vue'

const store = useProductsStore()
const counter = computed(()=>{
    return store.countFavorite
})
console.log(counter)
</script>

<style scoped>
nav {
    text-align: center;
    background-color:darkslategrey;
    padding: 0.5rem 0;
}
.link {
    text-decoration: none;
    color: whitesmoke;
    margin: 1rem;
}
#counter {
    background-color: red;
    padding: 0 1% 0 1%;
    border-radius: 50%;
}
</style>