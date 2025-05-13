<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList
    :products="products"
    @add-to-cart="onAddToCart"
    />
    <hr>
    <p>총 금액 : {{ totalPrice }}원</p>
    <h2>장바구니</h2>
    <ul>
      <Cart 
      v-for="item in cart" 
      :key="item.id" 
      :product="item"
      @remove-from-cart="onRemoveFromCart"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0


const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cart = ref([])

const onAddToCart = (product) => {
  cart.value.push(product)
}

const onRemoveFromCart = (product) => {
  cart.value = cart.value.filter(item => item.id !== product.id)
}

const totalPrice = computed(() => {
  return cart.value.reduce((total, item) => total + item.price, 0)
})
</script>
