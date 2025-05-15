<template>
  <div>
    <!-- <h1>Example</h1>
    <p>state:{{ store.count }}</p>
    <p>getters: {{ store.doubleCount }}</p>
    <button @click="store.increment">store.increment</button> -->
</div>
</template>

<script setup>
  import { useCounterStore } from '../stores/counter';
  const store = useCounterStore()
  console.log(store.count)
</script>

<style scoped>

</style>