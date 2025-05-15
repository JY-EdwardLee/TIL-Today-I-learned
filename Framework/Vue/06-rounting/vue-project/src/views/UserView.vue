<template>
    <div>
        <h1>user Page</h1>
        <button @click="goHome">HOME</button>
        <h2>현재 경로에 관련된 어떤 정보들은 {{ $route.params }}</h2>
        <h2>현재 경로에 관련된 어떤 정보들은 {{ $route.params.id }}</h2>
        <!-- post/profile 전환 -->
        <RouterLink :to="{name:'user-profile'}">Profile</RouterLink>
        <RouterLink :to="{name:'user-post'}">Post</RouterLink>
        <!-- 중첩된 자식 -->
        <RouterView />
    </div>
</template>

<script setup>
// route 기능은 우리가 프로젝트에 추가한 vue-route가 가지고 있음
import {useRoute, useRouter, RouterView, RouterLink, onBeforeRouteLeave} from 'vue-router'

onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('갈꺼냐')
    if (answer === false) {
        return false
    }
})

const route = useRoute()
const router = useRouter()
const goHome = ()=>{
    // 어디로 이동할 수 있음
    router.push({name: 'home'})
}
console.log(route)
console.log(router)
</script>

<style scoped>

</style>