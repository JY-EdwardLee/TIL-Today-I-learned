<template>
<div>
    <ChildPage 
    v-for="child in children"
    :key="child"
    :child="child"
    @give-me-allowance="updateBalance"
    />
</div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30, balance: 100000 },
  { name: '김두리', age: 20, balance: 10000 },
  { name: '김서이', age: 10, balance: 1000 }
])

const updateBalance = (childu)=>{
    const niceGuy=children.value.find(child => child.name === childu.name)
    niceGuy.balance += 1000
}
</script>

<style scoped>

</style>