<template>
    <div>
        <!-- for문으로 반복처리 -->
        <TodoListItem 
        v-for="todo in store.todos"
        :key="todo.id"
        :todo="todo"
        />
    </div>
</template>

<script setup>
import TodoListItem from './TodoListItem.vue';
import { useCounterStore } from '@/stores/counter.js';

const store = useCounterStore()
const todos = store.todos
console.log(todos)
</script>

<style scoped>

</style>