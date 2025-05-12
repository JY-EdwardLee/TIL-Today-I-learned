<template>
  <div class="album">
    <h2 class="album-title">앨범 제목</h2>
    <ul class="song-list">
      <li class="song-item">노래 1</li>
      <li class="song-item">노래 2</li>
      <li class="song-item">노래 3</li>
    </ul>
  </div>
</template>

<script setup>
// Component logic will be added later
</script>

<style scoped>
.album {
  margin: 0.5rem;
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  background-color: #f9f9f9;
  min-width: 0; /* Prevent flex item from overflowing */
  flex: 1 1 calc(50% - 1rem); /* Two items per row with gap */
  box-sizing: border-box;
}

.album-title {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 1rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.song-list {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 0.9rem;
}

.song-item {
  padding: 0.25rem 0;
  border-bottom: 1px solid #eee;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.song-item:last-child {
  border-bottom: none;
}
</style>