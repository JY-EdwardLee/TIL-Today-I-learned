<template>
<h1>상세 프로필</h1>
<p>반갑습니다. {{ username }}입니다.</p>
</template>

<script setup>
import {ref} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()
const username = ref(route.params.username)
</script>

<style scoped>

</style>