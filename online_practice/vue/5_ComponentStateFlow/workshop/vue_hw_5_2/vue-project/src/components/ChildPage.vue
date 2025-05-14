<template>
<div class="template">
<h3>자식 페이지입니다</h3>
<p>{{child.name}}</p>
<p>{{ child.age }}</p>
</div>
</template>

<script setup>
const childProps = defineProps({
    child: {
        type: Object,
        required: true,
        default: null,
    }
})
console.log(childProps)
</script>

<style scoped>

</style>