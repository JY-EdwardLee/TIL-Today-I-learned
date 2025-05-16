<template>
<div class="card">
    <p>{{ product.name }}</p>
    <img :src="product.imagePath" alt="">
    <p>{{ product.price }}원</p>
    <button @click.prevent="onClickFavorite" >
        <span v-if="product.isFavorite">♥</span>
        <span v-else>♡</span>
    </button>
</div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useProductsStore } from '@/stores/products'
const props = defineProps({
    product:Object
})
const store = useProductsStore()
// const selectedProduct = ref(props.product)

const onClickFavorite = function() {
    // console.log(selectedProduct.value)
    store.toggleFavorite(props.product)
}
const isFavorite = computed(() => props.product.isFavorite)
</script>

<style scoped>
.card {
    width: 300px;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;;
    border: 1px rgb(218, 218, 218) solid;
    margin: 1rem;
}
img {
    width: 300px;
    height: 200px;
}
</style>