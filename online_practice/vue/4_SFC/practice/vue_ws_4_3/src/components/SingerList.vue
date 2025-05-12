<template>
<div v-for="singer in singers" :key="singer">
  <div class="singer-card">
    <h1>{{ singer.name }}</h1>
      <SingerDetail/>
    <p>가수 소개글</p>
  </div>
</div>
</template>

<script setup>
// 컴포넌트 로직
import {ref} from 'vue'
import SingerDetail from '@/singers/SingerDetail.vue';
const singers = ref([
  {name : 'adele'},
  {name : 'Weeknd'},
  {name : 'ariana grande'},
])
</script>

<style scoped>
.singer-card {
  border: 1px solid black;
  padding: 20px;
  border-radius: 8px;
  margin: 0 auto;
  text-align: center;
}

.img-container {
  width: 200px;
  height: 200px;
  margin: 0 auto 16px;
  overflow: hidden;
  border-radius: 50%;
}

img {
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