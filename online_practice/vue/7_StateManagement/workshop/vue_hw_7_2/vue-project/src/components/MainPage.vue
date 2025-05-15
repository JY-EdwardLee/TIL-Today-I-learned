<template>
    <div>
        <h1>pinia 연습하기</h1>
        <ParentPage
        v-for="family in store.familyInfo"
        :key="family.familyName"
        :family="family"
        />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/family';
import ParentPage from './ParentPage.vue';
const store = useCounterStore()
</script>

<style scoped>
</style>