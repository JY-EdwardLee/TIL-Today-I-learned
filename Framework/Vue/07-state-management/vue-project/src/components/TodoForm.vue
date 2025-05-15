<template>
  <!--  -->
    <form @submit.prevent="onAddToto">
    <input type="text" v-model="todoText">
    <button>CREATE</button>
  </form>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter.js';
const store =useCounterStore()

const todoText = ref('')
const onAddToto = function() {
  store.addTodo(todoText.value)
  todoText.value=''
}
</script>

<style scoped>

</style>