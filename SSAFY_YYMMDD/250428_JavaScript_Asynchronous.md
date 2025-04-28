# Asynchronous JS (면접 단골)

### 비동기

- Synchronous (동기)
    - 프로그램의 실행 흐름이 **순차적으로 진행**
        
        ⇒ 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식
        
    - 반복이 완료될 때까지 다음 작업이 실행되지 않음
        
        ```jsx
        console.log('작업 1 시작')
        
            const syncTask = function () {
              for (let i = 0; i < 1000000000; i++) {
                // 반복 실행 동안 잠시 대기
              }
              return '작업 완료'
            }
        
            const result = syncTask()
            console.log(result)
        
            console.log('작업 2 시작')
        
            // 출력결과
            // 작업 1 시작
            // (반복 실행 동안 잠시 대기)
            // 작업 완료
            // 작업 2 시작
        ```
        
- Asynchronous (비동기)
    - 특정 작업의 실행이 완료될 때까지 기다리지 않고 다음 작업을 즉시 실행하는 방식
        
        ⇒ 작업의 완료 여부를 신경 쓰지 않고 **동시에 다른 작업들을 수행할 수 있음**
        
        ```jsx
        console.log('작업 1 시작')
        
            const asyncTask = function (callBack) {
              setTimeout(() => {
                callBack('작업 완료')
              }, 3000)
            }
        
            asyncTask((result) => {
              console.log(result)
            })
        
            console.log('작업 2 시작')
        
            // 출력결과
            // 작업 1 시작
            // 작업 2 시작
            // 작업 완료
        ```
        
    - 특)
        - 병렬적 수행
        - 당장 처리를 완료할 수 없고 **시간이 필요한 작업들**은 백그라운드에서 실행되고 **빨리 완료되는 작업부터 처리**

### Single Thread 언어, JavaScript

- Thread란?
    - 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
- JavaScript는 싱글 쓰레드 언어인데 어떻게 비동기 처리를 할까?

### → JavaScript Runtime

- 우리는 자바스크립트를 ‘브라우저’ 또는 ‘Node.js’에서 동작 시킨다.
    - 브라우저가 도와줄 것
- JavaScript가 비동기 처리할 수 있도록 도와주는 환경 필요
    - 비동기 처리 관련 요소
        1. JS Engine의 Call Stack
            - 요청이 들어올 때마다 순차적 처리 Stack (LIFO)
            - 기본적이 JS Single Thread 작업 처리
        2. Web API
            - JS 엔진이 아닌 브라우저 에서 제공하는 runtime 환경
            - 시간이 소요되는 작업을 처리
        3. Task Queue
            - 비동기 처리된 Callback 함수가 대기하는 Queue
        4. Event Loop
            - 태스크(작업)가 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고, 처리할 태스크가 없는 경우엔 잠든느, 끊임없이 돌아가는 자바스크립트 내 루프
            - Call Stack과 Task Queue를 지속적으로 모니터링
            - Call Stack이 비어 이는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push
    - 비동기 처리 방식
        1. Call stack으로 들어간 후 처리된다. (LIFO)
        2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 함
        3. Web API에서 처리가 끝난 작업은 곧바로 Call Stack으로 들어가지 못하고 Task Quere에 순서대로 들어간다.
        4. Event Loop가 Call stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보낸다.

### AJAX (Asynchronous JavaScript and XML)

- Ajax (Asynchronous JavacScript and XML)
    - 비동기적인 웹 어플리케이션 개발을 위한 기술
- Ajax 정의
    - XMLHttpRequet 기술을 사용해 복잡하고 동적인 웹페이지를 구성하는 프로그래밍 방식
    - 브라우저와 서버 간 데이터를 비동기적으로 교환하는 기술
    - Ajax를 사용하면 페이지 전체를 새로고침 하지 않고도 동적으로 불러와 화면을 갱신할 수 있음
    - Ajax의 ‘x’는 XML이라는 데이터 타입을 의미하지만, 실제로는 JSON을 더 많이 사용
- Ajax 목적
    1. 비동기 통신
        - 웹 페이지 전체를 새로고침하지 않고 서버와 데이터를 주고받을 수 있음
    2. 부분 업데이트
        - 전체 페이지가 다시 로드되지 않고 HTML페이지 일부 DOM만 업데이트
        - 페이지 일부분만 동적으로 갱신 가능
    3. 서버 부하 감소
        - 필요한 데이터만 요청하므로 서버 부하 줄일 수 있음

### XMLHttpRequset 객체

- 웹 브라우저와 서버 간의 비동기 통ㅇ신을 가능하기 하는 JS 객체
- 기능
    - JS로 HTTP 요청할 수 있는 객체
    - 서버로 부터 데이터를 가져오거나 보낼 때 새로고 침 없이 가능
        
        ⇒ 모든 데이터 타입 가능
        
- Ajax의 원리
    1. XHR 객체 생성 및 요청
    2. HTML응답이 아닌 JSON응답을 보냄
        
        → 데이터만 받아와서 새로고침 X
        → 데이터 처리의 일부분이 이제는 클라언트 쪽에서 처리됨
        
- 이벤트 핸들러도 비동기 프로그래밍이다.
    - 이번엔 이벤트 핸들러를 XHR 객체에 연결해 동작해보자

### Axios (라이브러리임)

: 브라우저와 Node.js에서 사용할 수 있는 Promise기반의 HTTP 클라이언트 라이브러리

→ 얘가 HTTP 요청을 보낼 거임

- 정의 및 특징
    - XHR 객체 생성
    - 간편한 API로 Promise 기반 비동기 요청 처리
    
    ⇒ 주로 웹 어플리케이션에서 버서와 통신할 때 사용
    
- Ajax를 활용한 클라이언트 서버 간 동작
    - XHR 객체 생성 및 요청 → 응답 데이터 생성 → JSON 데이터 응답→ Promise 객체 데이터를 활용해 DOM 조작
- axios는
    - 어떻게 ⇒ get, post , …
    - 어디에 ⇒ url
    - data를 담아서 보낼 수도 있음
    
    를 정의해 두면 함수를 호출할 때 해당 요청을 XHR 객체로 보내고 그 응답은 아랫 줄
    
- 객체를 요청으로 보내면
    - 성공했을 때는 response
    - 실패 했을 때는 error

### then & catch 특징

- then
    - 성공하면   callback 실행
    - callback은 이전 자겅ㅂ의 성공 결과를 ㄴ인자로 전달받음
- catch
    - then이 한번이라도 실패하면callback 실행
    - callback은 이전 작업의 실패 객체를 인자로 전달 받음
- 동작 순서
    - 서버가 보내준 응답 정보를 then에서 인자로 사용
    - 그 다음에 then에서는 넘겨받은 데이터를 또 사용 가능

### AJAX와 Axios 정리

- Ajax (개념이자 접근 방식)
    - 하나의 특정한 기술을 의미하는 것이 아니라, 비동기적 웹 어플리케이션 개발에 사용하는 기술들의 집합을 지칭
- Axios (도구)
    - 라이브러리

### Callback과 Promise

- 비동기 처리의 특성
    - 완료되는 순서에 따라 처리
- 처리의 어려움
    - 코드 실행 순서가 불명확함
    - 결과를 정확히 예측하며 코딩하기 어려움
- **비동기 콜백**
    - 순차적으로 동작할 수 있게 함
        
        ⇒ 작업의 순서와 동작을 제어하거나 결과를 처리하는 데 사용
        
    - 비동기 요청이 끝나야 동작하도록 callback() 함수를 실행
- 한계
    - 위 과정을 반복하다 보면 ⇒ 콜백 지옥 발생
- **프로미스**
    - then을 통해서 비동기 콜백의 한계를 극복할 수 있다.
    
    ⇒ 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능 제공
    
- **Axios**
    - 브라우저와 Node.js에서 사용할 수 있는 Promise 기반 HTTP 클라언트 라이브러리
- then & catch의 chaining
    - then과 catch는 모두 항상 promise 객체를 반환
        
        ⇒ 계속해서 chaining 가능
        
- why Promise?
    1. 실행 순서의 보장 ⇒ 비동기 작업의 실행 순서 예측 가능
    2. 유연한 비동기 처리
    3. 체이닝을 통한 연속적인 비동기 처리
    4. 에러 처리의 일원화