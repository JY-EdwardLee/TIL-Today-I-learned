<template>
    <h2>장바구니 페이지</h2>
    <div class="list">
    <ProductDetail 
    v-for="product in likedProduct"
    :key="product.id"
    :product="product"
    />
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useProductsStore } from '@/stores/products';
import ProductDetail from '@/components/ProductDetail.vue';
const store = useProductsStore()
const likedProduct = computed(() => 
  store.products.filter(product => product.isFavorite === true)
)
</script>

<style scoped>

</style>