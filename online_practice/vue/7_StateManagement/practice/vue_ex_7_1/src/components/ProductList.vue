<template>
<div>
    <ul v-for="product in store.products">
        <li>{{ product.id }} - {{ product.title }} - {{  product.body }}</li>
    </ul>
</div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const store = useProductStore()
</script>

<style scoped>

</style>