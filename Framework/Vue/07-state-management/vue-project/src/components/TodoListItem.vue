<template>
    <div>
        <!-- 속성에 넣는 것과 template syntax 작성방법 다름 -->
        <input type="checkbox" :id="todo.id" v-model="isDone">
        <!-- label의 for오 같은 id를 찾아서
         label에 작성된 textContent를 click 하면, -->
        <label for="todo.id">{{ todo.title }}</label>
        <button @click="onDeleteTodo">삭제</button>
    </div>
</template>

<script setup>
import {ref, watch} from "vue"
import { useCounterStore } from '@/stores/counter.js';
const props = defineProps({
    todo: Object
})
console.log(props.todo)
const store = useCounterStore()
const isDone = ref(props.todo.isDone)

watch(isDone, () => {
    store.UpdateTodo(props.todo.id)
})

const onDeleteTodo = function() {
    store.deleteTodo(props.todo.id)
}
</script>

<style scoped>

</style>