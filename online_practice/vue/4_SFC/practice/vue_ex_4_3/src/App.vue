<template>
  <div>
    <gallery-header />
    <gallery-list />
  </div>
</template>

<script setup>
import GalleryHeader from '@/components/Header.vue'
import GalleryList from '@/components/GalleryList.vue'
</script>

<style>
body {
  padding-top: 76px; /* 헤더 높이만큼 패딩 추가 */
}

.card {
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}
</style>
