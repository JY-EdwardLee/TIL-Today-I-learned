<template>
<li>
  {{ product.name }} - {{ product.price }}원
  <button @click="clickRemove()">삭제</button>
</li>
</template>

<script setup>
const props = defineProps({
  product: {    
    type: Object,
    required: true
  }
})
const emit = defineEmits(['removeFromCart'])

const clickRemove = () => {
    emit('removeFromCart', props.product)
}
</script>

<style scoped>

</style>