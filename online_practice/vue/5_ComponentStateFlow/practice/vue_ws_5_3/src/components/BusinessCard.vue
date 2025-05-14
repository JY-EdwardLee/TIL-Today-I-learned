<template>
<div>
    <h2>명함 목록</h2>
    <div class='card-list'>
    <businessCardDetail
    v-for="businessCard in businessCards"
    :key="businessCard.name"
    :businessCard="businessCard"
    @delete-card="deleteCard"
    />
    </div>
</div>
</template>

<script setup>
import {ref} from 'vue'
import businessCardDetail from './businessCardDetail.vue'

const businessCards = ref([
    {name:'일론 머스크', title:'테슬라 테크노킹'},
    {name:'래리 엘리슨', title:'오라클 창업주'},
    {name:'빌 게이츠', title:'마이크로소프트 공동창업주'},
    {name:'래리 페이지', title:'구글 공동창업주'},
    {name:'세르게이 브린', title:'구글 공동창업주'},
])

const deleteCard = (bizcard)=> {
    businessCards.value = businessCards.value.filter(card=>card.name!==bizcard.name)
}
</script>

<style scoped>
.card-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
}
</style>