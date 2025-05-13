<template>
<div class="business-card">
    <h2>이름 : {{businessCard.name}}</h2>
    <p>직함 : {{businessCard.title}}</p>
</div>
</template>

<script setup>
defineProps({
    businessCard: Object,
})
</script>

<style scoped>
.business-card {
    border: 1px solid #ccc;
    padding: 1rem;
    margin: 1rem;
    width: 300px;
}
</style>