<template>
<li>
    {{ product.id }} - {{ product.title }} - {{ product.body }}
    <button @click.prevent="deleteProduct(product.id)">delete</button>
</li>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const props = defineProps({
    product:Object
})
const store = useProductStore()
const deleteProduct = function(selected) {
    console.log(selected)
    store.deleteProduct(selected)
}
</script>

<style scoped>

</style>