import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const products = ref([])
  axios({
    method:'get',
    url: 'https://jsonplaceholder.typicode.com/posts',
  }) .then((request)=>{
    for (let i=0; i < request.data.length; i++) {
      products.value.push(request.data[i])
    }
  }) .catch((error)=>{
    console.log(error)
  })
  console.log(products)   

  const productCount = computed(() => products.value.length)

  const deleteProduct = function (productId) {
    // 요소를 직접 수정하는 대신에 splice 메서드를 사용하여 새로운 배열을 생성하여 상태를 업데이트
    const index = products.value.findIndex(product => product.id === productId)
    if (index !== -1) {
      products.value.splice(index, 1)
    }
  }

  return { products, productCount, deleteProduct }
})
