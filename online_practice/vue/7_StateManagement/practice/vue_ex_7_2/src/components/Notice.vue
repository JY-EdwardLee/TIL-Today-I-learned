<template>
<p> 총 상품 개수 : {{ store.total }}</p>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const store = useProductStore()

</script>
<style scoped>

</style>