# Controlling Event

## 이벤트

### 웹에서의 이벤트

- 웹에서의 모든 동작은 **이벤트 발생과 함께 한다.**

### event

- 웹페이지 상에서 ‘무언가 일어났다는 신호 또는 사건’
⇒ 사용자가 버튼을 클릭하거나, 키보드를 누르거나, 입력 필드에 값을 변경하는 행위 등
- DOM 요소와 이벤트
    - 모든 DOM요소는 다양한 이벤트를 발생시킬 수 있음
- ‘event’ object
    - 이벤트 발생 순간의 상황과 관련된 상세 정보를 담고 있음
    - 구체적인 정보를 참조할 수 있음
- DOM요소에서 event가 발생하면, 해당 event는 연결된 이벤트 처리기(event handler)에 의해 처리됨

### event handler

- 특정 이벤트가 발생했을 때 실행되는 (콜백)함수
    
    ⇒ 보통 **addEventListener**를 통해 DOM 요소에 등록
    
- .addEventListener()
    - 이벤트가 발생했을 때 실행할 이벤트 핸들러를 특정 DOM요소에 **등록하는 메서드**
        
        ⇒ 이벤트 핸들러를 DOM 요소에 ‘연결’하는 역할을 담당
        
    
    e.g. handClick 함수가 이벤트 핸들러이며, button.addEventListener()는 그 핸들러를 click 이벤트에 연결해주는 역할
    
    ```jsx
    EventTarget.addEventListener(type, handler) //(수신할 이벤트, 핸들러)
    ```
    
    ```jsx
    <body>
      <button>버튼</button>
    
      <script>
        const button = document.querySelector('body > button')
    
        // 이벤트 핸들러
        const handleClick = function () {
          window.alert('버튼이 클릭 되었습니다!')
        }
    
        // addEventListener 메서드를 이용해 버튼에 이벤트 핸들러를 등록
        button.addEventListener('mousemove', handleClick)
      </script>
    </body>
    ```
    
- addEventListener 함수의 handler 영역에 직접 함수를 써줘도 된다.
- 이벤트 객체 전달.
    - 이벤트 발생 시, 이벤트 객체는 자동으로 이벤트 핸들러 함수에 인자로 전달됨
    - 핸들러 함수는 이 인자를 통해 이벤트에 대한 상세 정보에 접근하고 적절한 동작을 수행
    
    ※ event 객체에는 다양한 method가 있음 잘 활용 바람
    

### 버블링

- 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들라가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
- 가장 최상단의 조상 요소를 만들 때까지 이 과정 반복
- why 버블링?
    - 각 버튼의 공통 조상인 div 요소에 이벤트 핸들러 단 하나만 할당

⇒ 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물속 거품과 닮아

- currentTarget & target
    - currentTarget
        - ‘현재’ 속성
        - 항상 이벤트 핸들러가 연결된 요소만을 참조
        - this와 같음
    - target
        - 실제 이벤트가 시작된 요소

### 캡쳐링

- 사실 버블링처럼 위로 올라가는 것 같지만
- 실제로는 최상위 요소에서 찾아서 와서 다시 올라가는 것이다.

- 이벤트 기본 동작 취소하기
    - HTML의 각 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해되는 경우가 있음
    - .preventDafault()
        
        : 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정