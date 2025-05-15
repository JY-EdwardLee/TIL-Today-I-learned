import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  // 사용자 값 CUD 할 때 반응하는 todos
  const todos = ref([
    // input:checkbox에 쓰일 id, v-for로 순회할 key 
    {id: id++,  title: 'vue 공부', isDone: false },
    {id: id++,  title: 'js 공부', isDone: false },
    {id: id++,  title: 'djnago 공부', isDone: true },
  ])
 const addTodo = function(todoText) {
    todos.value.push({
      id:id++,
      isDone:false,
      title: todoText,
    })
 }

 const deleteTodo = function(selectedId) {
  todos.value = todos.value.filter(todo => todo.id != selectedId)
 }

 const UpdateTodo = function(selectedId) {
    todos.value  = todos.value.map((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
 }
  return { 
    todos,
    addTodo, deleteTodo, UpdateTodo }
}, { persist: true })