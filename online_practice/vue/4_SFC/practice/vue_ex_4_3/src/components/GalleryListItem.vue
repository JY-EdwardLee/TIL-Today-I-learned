<template>
  <div class="card h-100">
    <img 
      src="@/assets/sample.png" 
      class="card-img-top" 
      alt="Sample Image"
    >
    <div class="card-body d-flex flex-column">
      <h5 class="card-title">Card title {{ number }}</h5>
      <p class="card-text flex-grow-1">
        Some quick example text to build on the card title and make up the bulk of the card's content.
      </p>
      <gallery-list-item-button />
    </div>
  </div>
</template>

<script>
import GalleryListItemButton from '@/components/GalleryListItemButton.vue'

export default {
  name: 'GalleryListItem',
  components: {
    GalleryListItemButton
  },
  props: {
    number: {
      type: Number,
      required: true
    }
  }
}
</script>
