<template>
  <div class="singer-list">
    <div v-for="singer in singers" :key="singer.name" class="singer-card">
      <h1>{{ singer.name }}</h1>
      <SingerDetail/>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SingerDetail from './singers/SingerDetail.vue';

const singers = ref([
  { name: 'Adele' },
  { name: 'Maroon 5' },
  { name: 'Dua Lipa' }
])
</script>

<style scoped>
.singer-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.singer-card {
  border: 1px solid black;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  width: 100%;
  box-sizing: border-box;
}

.img-container {
  width: 100%;
  height: 200px;
  overflow: hidden;
  border-radius: 8px;
  margin: 0 auto 16px;
}

.img-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

h1 {
  margin: 0 0 16px 0;
  font-size: 1.5rem;
}

p {
  margin: 16px 0 0 0;
  font-size: 1rem;
  line-height: 1.5;
}
</style>