<template>
    <p>번호: {{ post.id }}</p>
    <p>제목: {{ post.title }}</p>
    <p>내용: {{ post.content }}</p>
</template>

<script setup>
import {ref, computed} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()
const posts = ref([
    {id: 1, title: 'Post 1', content: 'Content 1'},
    {id: 2, title: 'Post 2', content: 'Content 2'},
    {id: 3, title: 'Post 3', content: 'Content 3'},
])
const post = computed(() =>
    posts.value.find(p => p.id == route.params.id)
)
console.log(route.params.id)
</script>

<style scoped>

</style>