<template>
    <div>
        <h1>메인 페이지</h1>
        <div v-for="balance in store.balances" :key="balance.name">
            <p>이름 : {{ balance.name }}</p>
            <p>잔고 : {{ balance.balance }}</p>
            <button @click="goToUpdate(balance.name)">updateBalance</button>
            <hr>
        </div>
    </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/blanace';
import { useRouter } from 'vue-router';
const store = useBalanceStore()

const router = useRouter()
const goToUpdate = function(name) {
    router.push({name:'update', params:{name:name}})
}

</script>

<style scoped>

</style>