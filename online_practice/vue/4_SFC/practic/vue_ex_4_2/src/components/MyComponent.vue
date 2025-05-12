<!-- Bootstrap을 사용한다.
index.html의 적절한 위치에 Bootstrap CDN을 작성한다.
MyComponent의 header 요소는 페이지의 제목이 출력된다.
항상 페이지 상단에 고정된다.
제목 텍스트는 상하좌우 가운데 정렬된다.
MyComponent의 main 요소는 메인 갤러리 영역이다.
Bootstrap Card 컴포넌트가 4개 사용된다.
Card는 정수 4 값을 가지는 반응형 변수 'numberOfItems' 와 v-for를 활용해 출력된다.
각 Card의 이미지는 assets/ 폴더에 위치한 sample 이미지를 사용한다.
Card는 화면 너비에 따라 반응형 레이아웃을 가진다.
화면 너비가 576 이상이면 한 행에 2개씩 출력된다.
화면 너비가 768 이상이면 한 행에 3개씩 출력된다.
요구사항 외 스타일링은 실행결과를 참고해 자유롭게 구성한다. -->

<template>
    <header class="fixed-top bg-white py-3 shadow-sm">
      <h1 class="text-center m-0">My Gallery</h1>
    </header>

    <main class="container mt-5 pt-4">
      <div class="row g-4">
        <div 
          v-for="number in numberOfItems" 
          :key="number"
          class="col-12 col-sm-6 col-md-4"
        >
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
              <a href="#" class="btn btn-primary mt-auto">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>
    </main>
</template>

<script setup>
import { ref } from 'vue'

const numberOfItems = ref(4)
</script>

<style scoped>
body {
  padding-top: 76px; /* 헤더 높이만큼 패딩 추가 */
}

.card {
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

</style>
