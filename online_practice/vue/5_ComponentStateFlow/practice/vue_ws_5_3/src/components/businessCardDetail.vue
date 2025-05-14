<template>
<div class="business-card">
    <h2>이름 : {{businessCard.name}}</h2>
    <p>직함 : {{businessCard.title}}</p>
    <button @click="deleteButton(businessCard)">명함 삭제</button>
</div>
</template>

<script setup>
defineProps({
    businessCard: Object,
})
const emit = defineEmits(['deleteCard'])
const deleteButton = (card) => {
    emit('deleteCard', card)
}
</script>

<style scoped>
.business-card {
    border: 1px solid #ccc;
    padding: 1rem;
    margin: 1rem;
    width: 300px;
}
</style>