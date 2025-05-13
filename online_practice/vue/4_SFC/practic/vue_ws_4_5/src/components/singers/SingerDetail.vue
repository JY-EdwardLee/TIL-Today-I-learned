<template>
  <div class="singer-detail">
    <div class="img-container">
      <img src="@/assets/singer.jpg" alt="가수 이미지">
    </div>
    <div class="albums">
      <SingerAlbum />
      <SingerAlbum />
    </div>
  </div>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue';
</script>

<style scoped>
.singer-detail {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin: 1rem auto 0;
  max-width: 600px;
  width: 90%;
}

.img-container {
  width: 100%;
  max-width: 200px;
  height: 200px;
  border-radius: 8px;
  overflow: hidden;
  margin: 0 auto;
}

.img-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.albums {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  width: 100%;
}

.albums > * {
  flex: 1 1 calc(50% - 0.5rem);
  min-width: 0;
}
</style>