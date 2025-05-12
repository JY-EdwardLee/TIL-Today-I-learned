<template>
  <div class="singer-card">
    <h1>가수 이름</h1>
    <div class="img-container">
      <img src="@/assets/singer.jpg" alt="가수 이미지">
    </div>
    <p>가수 소개글</p>
  </div>
</template>

<script setup>
// 컴포넌트 로직
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