<template>
  <h1>App.vue</h1>
  <!-- userNmae 변수에 든 값을 Parent 컴포넌트에게 prop -->
   <!-- prop 받을 데이터가 담길 벼누명은 HTML 속성 형태로 작성한다. -->
  <!-- 내 상태를 HTML 상태에 묶어야 한다. -->
   <Parent 
    :user-name="userName"
    @change-user-name="onChangeUserName"
  />
</template>

<script setup>
 import Parent from '@/components/Parent.vue'
 import {ref} from 'vue'
 const userName = ref('Alice')
 const onChangeUserName = () => {
  userName.value = 'Chalrie'
 }
</script>

<style scoped>

</style>