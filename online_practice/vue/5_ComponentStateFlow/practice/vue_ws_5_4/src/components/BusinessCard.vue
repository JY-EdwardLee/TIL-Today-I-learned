<template>
<div>
    <h2>명함 목록</h2>
    <p v-if="numberOfCards > 0">현재 보유중인 명함 수 : {{ numberOfCards }}</p>
    <div class='card-list' v-if="numberOfCards > 0">
    <businessCardDetail
    v-for="businessCard in businessCards"
    :key="businessCard.name"
    :businessCard="businessCard"
    @delete-card="deleteCard"
    />
    </div>
    <p v-else>명함이 없습니다. 새로운 명함을 추가해주세요.</p>
</div>
</template>

<script setup>
import {ref, computed} from 'vue'
import businessCardDetail from './businessCardDetail.vue'

const businessCards = ref([
    {name:'일론 머스크', title:'테슬라 테크노킹'},
    {name:'래리 엘리슨', title:'오라클 창업주'},
    {name:'빌 게이츠', title:'마이크로소프트 공동창업주'},
    {name:'래리 페이지', title:'구글 공동창업주'},
    {name:'세르게이 브린', title:'구글 공동창업주'},
])

const numberOfCards = computed(() => businessCards.value.length)

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