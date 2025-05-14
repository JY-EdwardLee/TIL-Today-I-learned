<template>
    <h1>학생 상세 정보 목록입니다.</h1>
<div v-for="student in Students">
    <p @click="StudentDetail(student.name)">{{ student.name }}</p>
</div>
</template>

<script setup>
import {ref} from 'vue'
import { RouterLink, useRouter } from 'vue-router';
const router = useRouter()
const Students = ref([
    {name:'김하나'},
    {name:'김두리'},
    {name:'김세찌'}
])
const StudentDetail = (name)=>{
    router.push({name:'StudentDetail', params:{'name':name}})
}

</script>

<style scoped>

</style>