<template>
  <nav>
    <RouterLink
    :to="{name:'main'}"
    >
    main
  </RouterLink>
  </nav>
  <div>
    <h1>pinia + router 연습하기</h1>
    <RouterView />
  </div>
</template>

<script setup>
import MainPage from './components/MainPage.vue';
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>