<template>
<div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ account[0].name }}</p>
    <p>잔고 : {{ account[0].balance }}</p>
    <button @click="addBalance(account)">+</button>
</div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/blanace';
import { useRoute } from 'vue-router';
const route =useRoute()
const store = useBalanceStore()
const balances = store.balances
console.log(balances)
const account = balances.filter(balance=>balance.name===route.params.name)
console.log(account)
const addBalance = function() {
    store.addBalance(account[0])
}

</script>

<style scoped>

</style>