# Basic Syntax02

## 객체

### object

: 키로 구분된 데이터 집합을 저장하는 자료형

- 객체 구조
    - 중괄호 {}를 이용해 작성
    - key : value 쌍
        
        ※key는 문자형만 허용 (띄어쓰기가 있을 때만 “” 따옴표 붙이기)
        
        ※ value는 모든 자료형 허용 (function도 - 단, 선언식으로는 작성 불가능, arrow 활용 가능)
        
- 속성 참조법
    - 점(’.’, chaining operator) 또는 대괄호 []를 이용해서 접근
    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호만 접근 가능
    - 속성 추가/수정
        - **object.key(없는 값) = value**
            - 하면 생김
        - **objec.key(있는 값) = new value**
            - 하면 override 됨
    - 속성 삭제
        - **delete object.key**
    - in 연산자
        - **key in object** // true or false

### 메서드

: 객체 속성에 정의된 함수

- 사용 예시
    - object.method() 방식으로 호출
    - 객체의 ‘행동’을 정의함

### this

- Method
    
    : 객체 속성에 정의된 함수
    
    ⇒ this 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 잇음
    
- ‘this’ keyword
    
    : 함수나 메서드를 호출한 객체를 가리키는 키워드
    
    ⇒ 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
    

※ window = 최상위 객체

★JS에서 this 함수를 호출하는 방법에 따라 가리키는 대상이 다름

| 호출 방법 | 대상 |
| --- | --- |
| 단순 호출 | 전역 객체 |
| 메서드 호출 | 메서드를 호출한 객체 |
- JS의 함수는 호출될 때 this를 암묵적으로 전달 받음
- JS에서 this는 함수가 호출되는 방식에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해 JS의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨

### 추가 객체 문법

- 단축
    1. 단축 속성
        
        ```jsx
        const name = 'aicle'
        const age = 30
        const user = {
        	name, age
        	}
        ```
        
    2. 단축 메서드
        
        ```jsx
        const myObj1 = {
        	myFunc() {
        		return 'Hello'
        		}
        	}
        ```
        
- 계산된 속성
    - 키가 대괄호 []로 둘러싸여 있는 속성
        - ⇒ 고정된 값이 아닌 변수 값을 사용할 수 있음
- 구조 분해 할당 (destructing assignment)
    
    ```jsx
        const userInfo = {
          firstName: 'Alice',
          userId: 'alice123',
          email: 'alice123@gmail.com'
        }
        const { firstName, userId, email } = userInfo
    ```
    
- Object with ‘전개 구문’
    - 객체 복사
        - 객체 내부에서 객체 전개
    - 얕은 복사에 활용 가능
        
        ```jsx
            const obj = { b: 2, c: 3, d: 4 }
            const newObj = { a: 1, ...obj, e: 5 }
            console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
        ```
        
- 유용한 객체 메서드
    - Obj.keys()
    - Obj.values()
- Optional chaining(’?.)
    - 사용법 : ?. (e.g. user.address.street)
    - 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
    - 만약 참조 대상이 null 또는 undefined라면 에러 대신 평가를 멈추고 undefined를 반환
    
    ```jsx
        // console.log(user.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
        console.log(user.address?.street) // undefined
    
        // console.log(user.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
        console.log(user.nonMethod?.()) // undefined
    
        console.log(user.address && user.address.street) // undefined
    
        console.log(myObj?.address) // Uncaught ReferenceError: myObj is not defined
    ```
    

### JSON (JavaScripot Object Notation)

- Key-Value 형태로 이루어진 자료 표기법
- JSON은 형식이 있는 문자열
    
    ⇒ 자료형 변경 필수
    
- Obj ↔ JSON 변환
    
    ```jsx
        const jsObject = {
          coffee: 'Americano',
          iceCream: 'Cookie and cream'
        }
    
        // Object -> JSON
        const objToJson = JSON.stringify(jsObject)
        console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
        console.log(typeof objToJson)  // string
    
        // JSON -> Object
        const jsonToObj = JSON.parse(objToJson)
        console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
        console.log(typeof jsonToObj)  // object
    ```
    

## 배열

### Object

: 키로 구분된 데이터 집합을 저장하는 자료형

⇒ 이제는 순서가 있는 collection이 필요

- Array
    
    : 순서가 있는 데이터 집합을 저장하는 자료구조
    
    ※ Negative indexing 조회 안됨, 근데 할당은 됨
    
    ※ 마지막 추가하고 싶으면 array[array.length - 1] = value
    
- 배열 구조
    - 

### 배열 메서드

- 주요 메서드
    
    
    | 메서드 | 역할 |
    | --- | --- |
    | push / pop | 배열 끝 요소를 추가 / 제거 |
    | unshift / shift | 배열 앞 요소를 추가 / 제거 |

### Array helper method

: 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음

- ES6에 도입
- 배열의 각 요소를 **순회**하며 각 요소에 대해 함수(**골백함수)**를 호출
- forEach(), **map()**, **filter()**, every(), some(), reduce() 등

⇒ 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징

### 콜백함수

: 다른 함수에 인자로 전달되는 함수

⇒ 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

| 메서드 | 역할 |
| --- | --- |
| filter | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |
| find | 콜백 함수의 반환 값이 참이면 해당 요소를 반환 |
| some | 배열의 요소 중 적어도 하나라도 콜백 함수를 통과하면 true를 반환하며 즉시 배열 순회 중지, 반면에 모두 통과하지 못하면 false를 반환 |
| every | 배열의 모든 요소가 콜백 함수를 통과하면 true를 반환, 반면에 하나라도 통과하지 못하면 즉시 false를 반환하고 배열 순회 중지 |
- forEach
    - 배열 내의 모든 요소 각각에 대해 함수 (콜백함수)를 호출
    
    ★ **반환 값 없음**
    
- forEach()
    
    ```jsx
    arr.forEach(callback(item[, index[, array]]))
    ```
    
    1. item : 처리할 배열의 요소
    2. index : 처리할 배열의 요소 인덱스 (선택 인자)
        
        = 값의 인덱스
        
    3. array: forEach를 호출한 배열 (선택인자)
        
        = 원본 arr의 값
        
    
    e.g.
    
    ```jsx
        const names = ['Alice', 'Bella', 'Cathy']
    
        // 일반 함수 표기
        names.forEach(function (name) {
          console.log(name)
        })
    
        // 화살표 함수 표기
        names.forEach((name) => {
          console.log(name)
        })
    
        // 활용
        names.forEach(function (name, index, array) {
          console.log(`${name} / ${index} / ${array}`)
        })
    ```
    
- map
    
    : 배열의 모든 요소에 대해 콜백 함수를 호출하고, 반환 된 호출 결과 값을 모아 **새로운 배열을 반환**