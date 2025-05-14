<template>
<div>
<p>이름 :{{ child.name }}</p>
<p>나이 : {{ child.age }}</p>
<p>용동 : {{ child.balance }}</p>
<button @click="buttonClick">용돈 좀 더주세요.</button>
</div>
</template>

<script setup>
const childProps = defineProps({
    child:{
        type: Object,
    }
})

const emit = defineEmits(['giveMeAllowance'])
const buttonClick = function() {
    emit('giveMeAllowance', childProps.child)
}
</script>

<style scoped>

</style>