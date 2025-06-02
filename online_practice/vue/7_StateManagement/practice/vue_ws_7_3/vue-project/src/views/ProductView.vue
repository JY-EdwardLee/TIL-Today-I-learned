<template>
    <h2>상품 목록 페이지</h2>
    <div class="list">
    <ProductDetail 
    v-for="product in store.products"
    :key="product.id"
    :product="product"
    />
    </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue';
import { useProductsStore } from '@/stores/products';

const store = useProductsStore()

</script>

<style scoped>
.list {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
</style>