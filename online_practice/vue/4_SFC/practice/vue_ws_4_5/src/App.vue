<script setup>
import SingerList from './components/SingerList.vue';
import MainPage from './components/MainPage.vue';
</script>

<template>
    <div style="text-align: center;">
    <h1>가수 목록</h1>
    <div>
        <MainPage />
    </div>
    <div>
        <SingerList />
    </div>
</div>
</template>

<style scoped>
</style>
