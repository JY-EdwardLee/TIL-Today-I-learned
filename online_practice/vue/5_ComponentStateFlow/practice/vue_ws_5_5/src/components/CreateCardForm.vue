<template>
  <v-card class="mx-auto" color="lighten-1" max-width="500">
    <v-card-title>
      <v-card-title class="font-weight-bold">명함 추가</v-card-title>
    </v-card-title>
    <v-card-text>
      <v-form @submit.prevent="createCardFunc" class="pa-4">
        <v-text-field
          v-model="name"
          label="이름"
          prepend-icon="mdi-account"
          outlined
          dense
          class="mb-3"
          required
        />
        <v-text-field
          v-model="title"
          label="직함"
          prepend-icon="mdi-card-account-details"
          outlined
          dense
          class="mb-3"
          required
        />
        <v-btn type="submit" color="primary" block class="mt-4">명함 추가</v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>


<script setup>
import {ref} from 'vue'
const name = ref('')
const title = ref('')
const emit = defineEmits(['createCard'])
const createCardFunc = (e) => {
    e.preventDefault()
    const card = {name: name.value, title: title.value}
    emit('createCard', card)
    name.value = ''
    title.value = ''
}

</script>
