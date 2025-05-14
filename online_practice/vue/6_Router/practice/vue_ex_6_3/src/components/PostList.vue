<template>
    <h2>{{ username }}작성한 게시글</h2>
<div>
    <ol>
    <PostListItem 
    v-for="post in posts"
    :key = post.id
    :post="post"
    />
    </ol>
</div>
<hr>
<RouterView />
</template>

<script setup>
import {ref} from 'vue'
import PostListItem from './PostListItem.vue'
import {useRoute, RouterView} from 'vue-router'
const route = useRoute()
const username = ref(route.params.username)

const posts = ref([
    {id: 1, title: 'Post 1', content: 'Content 1'},
    {id: 2, title: 'Post 2', content: 'Content 2'},
    {id: 3, title: 'Post 3', content: 'Content 3'},
])
</script>

<style scoped>

</style>