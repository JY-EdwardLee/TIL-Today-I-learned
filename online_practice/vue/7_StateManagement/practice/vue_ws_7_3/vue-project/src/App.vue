<template>
<nav>
<RouterLink :to="{name: 'home'}" class="link">Home</RouterLink>
<RouterLink :to="{name: 'products'}" class="link">Products</RouterLink>
<RouterLink :to="{name: 'favorite'}" class="link" >Favorits</RouterLink>
</nav>
<div>
    <RouterView />
</div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

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
</style>