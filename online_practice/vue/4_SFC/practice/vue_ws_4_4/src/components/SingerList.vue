<template>
  <div class="card">
    <h1>가수 이름</h1>
    <div class="img-container">
      <img src="../assets/singer.jpg" alt="가수 이미지">
    </div>
    <p>가수 소개글</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
.card {
    display: inline-block;
    width: 40%;
    margin: 20px;
}
h1 {
    color: orangered;
}
.img-container {
  width: 200px;
  height: 200px;
  margin: 0 auto 16px;
  overflow: hidden;
  border-radius: 50%;
}
</style>