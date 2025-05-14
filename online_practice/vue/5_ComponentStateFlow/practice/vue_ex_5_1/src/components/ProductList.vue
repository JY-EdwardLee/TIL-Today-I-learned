<template>
    <li>
        {{ product.name }} - {{ product.price }}
    </li>
</template>

<script setup>
defineProps({
    product: {
        type: Object,
        required: true,
    }
})
</script>

<style scoped>

</style>