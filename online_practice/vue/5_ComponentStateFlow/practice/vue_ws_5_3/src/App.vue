<template>
    <div class="container">
      <header>
        <div>
          <h1>명함 관리 페이지</h1>
        </div>
      </header>
      <main>
        <p>명함을 관리하는 페이지입니다. 여기에 명함목록이 표시됩니다.</p>
      </main>
      <article>
        <BusinessCard />
      </article>
      <footer>
        <p>© 2025 My Business Cards</p>
      </footer>
    </div>
  </template>
  
  <script setup>
import BusinessCard from './components/BusinessCard.vue'

</script>
  
  <style scoped>
  header div{
      text-align: center;
      padding: 1rem;
      margin: 1rem auto;
      width: 300px;
      background-color: #333;
      color: #fff;
  }
  
  main {
  text-align: center;
  }
  
  article {
  text-align: center;
  }
  
  .container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  footer {
    text-align: center;
    background-color: #d7d7d7;
    padding-top: 1rem;
    margin-top: auto;
  }
  </style>