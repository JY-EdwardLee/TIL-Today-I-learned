<template>
<div class="card">
    {{ product.name }}
    <img :src="path" alt="">
    {{ product.price }}
    {{ product.isFavorite }}
</div>
</template>

<script setup>
const props = defineProps({
    product:Object
})

const path = props.product.imagePath
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