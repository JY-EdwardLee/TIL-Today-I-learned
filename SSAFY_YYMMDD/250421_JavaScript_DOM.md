# DOM

### History of JavaScript

- 웹브라우저와 JAVA
    1. 웹의 탄성
        - Tim Berner-Lee가 만듬
            
            ⇒ 정적인 텍스트 페이지만 지원
            
    2. 웹 브라우저의 대중화
        - Netscape사가 만든 Netscape Navigator가 최초 (90% 점유율)
        
        ⇒ Netscape사는 웹의 동적인기능을 만들기 위한 프로젝트를 시작
        
    3. JavaScript의 탄생
        - Brendan Eich가 만든 Mocha를 개발
        - JavaScript로 이름 변경
    4. JavaScript 파편화
        - 인터넷 익스플로러가 Javascript 대신 JScript를 도입
    5. 1차 브라우저 전쟁
        - Netscape vs Microsoft
    
    5-1. 1차 브라우저 전쟁의 영향
    
    - 브라우저 마다 언어가 달라 개발에 어려움
    1. ECMAScript 출시
        - ECMAScript 표준 언어 정의하여 발표
        - JavasScript가 ECMA 표준에 따라 만듬
    2. 2차 브라우저 전쟁
        - IE가 웹 표준을 지키지 않음
        - 파이어 폭스가 대항
            - Jquery가 각광
    3. Chrome 브라우저의 등장
        - ECMA 표준을 아주 잘 지킴
        - 개발자들이 크롬에서 작업하기 쉬워짐
        - 특징
            - 호환성, 개발자 도구, 가벼운 프로그램
    4. 2차 브라우저 전쟁의 영향
        - 크롬의 성공을 보고, 타 브라우저들도 웹 표준 지킴
        - 그래서 이제는 Jquery 대신 Javascript 공부하게 됨

### ECMAScrip와 JavaScript

- JavaScript는 ECMA 표준을 구현한 구체적인 프로그래밍 언어
- 우리는 JS를 배우고 Vue를 쓰기 위해 Node.js를 쓸 꺼다
    
    ※ ES6 이후 버전의 문법인 것을 확인하고 공부해야 함
    

### JavaScript의 현재

- 현재는 Node.js 이후로 서버 사이드 개발에도 사용 됨 (express.js)

※ 키워드야 : CommonJS → 서버 사이드  모듈화 표준 제안 아이콘 추가

---

## 변수

### JS 문법 학습

- 식별자(변수명) 자성 규칙
    - 반드시 문자, 달러($) 또는 밑줄(’_’)로 시작
        - ⇒ 특별한 친구들에게 붙여준다. 고유의 변수
    - 대소문자를 구분
    - 예약어 사용 불가
        - for, if function 등
- **★식별자의 Naming case**
    - 카멜 케이스(camelCase)
        - 변수, 객체, 함수에 사용
            
            ※ 파이썬과 다르다
            
    - 파스칼 케이스(PascalCas)
        - 클래스, 생성자에 사용
    - 대문자 스네이크 케이스(SNAKE_CASE)
        - 상수(constants)에 사용
            
            e.g. .env 내의 API_KEY 같은 녀석들
            
- 변수 선언 키워드
    - 선언 키워드 3가지
        - let, const, ~~var(안 씀)~~
    - let
        - 블록 스콮(block scope)를 갖는 지역 변수 선ㄴ언
        - **재할당 가능 (LET A = ?, A = ??)**
        - **재선언 불가능 (LET B =?, LET B =??)**
        - ES6에서 추가
    - const
        - 블록 스코프를 갖는 지역 변수 선언
        - **재할당 불가능**
            
            ⇒ 선언하는 시점에 반드시 변수값이 선언되어야 한다.
            
        - **재선언 불가능**
        - ES6에서 추가
    
    - 블록 스코프
        - if, for, 함수 등의 중괄호({}) 내부를 가리킴
        - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

- const를 기본으로 사용하고, 필요할 때 let 사용
    - why const?
        - 코드의 의도 명확화
            - 해당 변수는 재할당되지 않을 것
            - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있게 해줌
        - 버그 예방
            - 의도치 않는 값 변경 오류 예방
            - 큰 규모의 프로젝트나 팀 작업에서 중요

### DOM

- 웹 블라우저의 JavaScript
    - 웹 페이지의 동적인 기능을 구현
- JS 실행 환경 종류
    1. HTML script 태그 안
    2. ~~js 확장자 파일~~ => node.js가 설치가 되야 사용 가능
    3. ~~브라우저 console~~ ⇒ 테스트 할 때 외에는 안 씀

### 문서 구조

- Document structure
    - HTML 문서는 상자들이 중첩된 형태로 볼 수 있음
    - HTML의 문서 구조를 하나의 객체들로 생각하면 좋다.
        
        ⇒ Docunet Object Model (문서 객체 모델)
        
- DOM
    - DOM API
        - 다른 프로그래밍 언어가 웹페이지에 접근 및 조작할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공
        - 웹 페이지를 구조화한된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
            
            ⇒ 문서 구조, 스타일, 내용들을 변경 가능
            
    - document 객체
        - 웹 페이지를 나타내는 DOM트리의 최상위 객체
            
            ⇒ HTML 문서의 모든 콘텐츠에 접근하고 조작할 수 있는 진입점
            
- DOM tree
    - HTML 태그를 나타내는 elements의 node는 문서의 구조를 결정
- DOM 핵심
    - 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API

- DOM 조작 시 기억해야 할 것
    - 웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기
        - 조작 순서
            1. 조작 하고자 하는 요소를 **선택** (또는 탐색)
            2. 선택된 요소의 콘텐츠 또는 속성을 **조작**
    - 선택 메서드
        - document.querySelector()
            - 요소 한 개 선택 (”.선택자”)
        - document.querySelectorAll()
            - 요소 여러 개 선택
    - querySelector(선택자)
        - 가장 먼저 나오는 선택자에 해당하는 요소
            - 다 보고 싶으면? querySelectorAll

### DOM 조작

1. 속성 조작
2. HTML 콘텐츠 조작
3. DOM 요소 조작
4. 스타일 조작

### 1. 속성 조작

1. 클래스 속성 조작
    - clasLit property : 요소의 ㅋㄹ래스 목록을 DOM  TokenList 형태로 반환
        - element.classList.add()
        - element.classList.remove()
        - element.classList.toggle()
            - 클래스가 조재하면 제거 false 반환
            - 존재하지 않으면 클래스 추가하고 true 반환)
2. 일반 속성 조작
    - Element.getAttribute() ⇒ 조회
    - Element.SetAttribute(name, value) ⇒ 설정
    - Element.removeAttribute() ⇒ 속성 제거

### 2. HTML 콘텐츠 조작

- ‘textContent’ property
    - 요소의 텍스트 콘텐츠를 표현
        
        e.g. <p> lorem </p>
        

### 3. DOM 요소 조작

- document.createElement(tagName)
    - tag 요소를 맘껏 만들 수 있다.
- Node.appendChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 추가된 Node 객체를 반환
- Ndoe.removechild()

### 4. style 조작

- html에서도 인라인 조작 잘 안했음
- 실질적으로는 안 씀
- 실제로는 클래스를 설정하고 add, remove 등으로 조절