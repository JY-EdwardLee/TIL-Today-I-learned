<template>
  <main class="container py-3">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div 
        v-for="number in numberOfItems" 
        :key="number"
        class="col"
      >
        <gallery-list-item :number="number" />
      </div>
    </div>
  </main>
</template>

<script>
import GalleryListItem from '@/components/GalleryListItem.vue'

export default {
  name: 'GalleryList',
  components: {
    GalleryListItem
  },
  data() {
    return {
      numberOfItems: 4
    }
  }
}
</script>
