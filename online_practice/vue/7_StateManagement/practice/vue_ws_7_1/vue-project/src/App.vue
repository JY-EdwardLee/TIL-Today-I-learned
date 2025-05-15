<template>
<nav>
<FavoritView />
<span>|</span>
<HomeView />
<span>|</span>
<ProductView />
</nav>

</template>

<script setup>
import FavoritView from './views/FavoritView.vue';
import HomeView from './views/HomeView.vue';
import ProductView from './views/ProductView.vue';

</script>

<style scoped>

</style>