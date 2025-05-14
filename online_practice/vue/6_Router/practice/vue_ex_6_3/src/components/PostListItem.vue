<template>
    <li>
    <RouterLink :to="{name:'post-detail', params:{id:post.id}}">{{post.title}}</RouterLink>
    </li>
</template>

<script setup>
import { RouterLink } from 'vue-router'
const props = defineProps({
    post:{  
        type: Object,
        required: true
    }
})
</script>

<style scoped>

</style>