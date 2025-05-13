<template>
<h1>부모 페이지입니다.</h1>
<div class="template">
<ChildPage 
v-for="child in children"
:key="child.name"
:child="child"
/>
</div>
</template>

<script setup>
import {ref} from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
    {'name': '김하나', age:30},
    {'name': '김snfl', age:20},
    {'name': '김tkdl', age:10},
])
</script>

<style scoped>

</style>