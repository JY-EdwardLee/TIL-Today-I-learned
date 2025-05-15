import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
    let id = 0
    const products = ref([
        {id: id++, title: 'Prd 1', body: 'quia et'},
        {id: id++, title: 'Prd 2', body: 'uo et'},
        {id: id++, title: 'Prd 3', body: 'reurqet'},
    ])
    return { products }
})
