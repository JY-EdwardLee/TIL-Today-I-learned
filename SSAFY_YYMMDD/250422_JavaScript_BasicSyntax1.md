# Basic syntax 01

## 데이터 타입

### 원시 자료형 vs 참조 자료형

- 원시 자료형 (Primitive type) ⇒ Number, String, Boolean, null, undefined
    
    : 원시적인 자료형, 프로그래머가 이용 가능한 가장 작은 단위
    
    → 변수에 값이 직접 저장되는 자료형 (불변, 값이 복사 - 참조값이 아닌 값을 직접 복사해서 할당, 스택 메모리에 직접 저장)
    
- 참조 자료형 (Reference type) ⇒ Objects, Array, Function
    
    : 갹체의 주소가 저장되는 자료형 (가변, 주소가 복사)
    

### 원시 자료형

- Number
    
    : **정수** 또는 **실수형** 숫자를 표현하는 타입
    
    → number에 숫자 관련 형태 다 저장 가능
    
    ※ infininy(무한대), NaN (Not a Number)
    
- String
    
    : 텍스트 데이터 표현 자료형
    
    → 문자열 연산 가능 (+)
    
    ※ 문자열 * 30 같은 거 하면 NaN 나옴
    
- Template literals (like formating)
    - 여러줄 쓰기 `` (back tick)
    - formating ⇒ `` 안에 $와 {}로 표기
- null과 undefined
    - null **프로그래머**가 의도적으로 값이 없음을 **나타낼 때**
    - undefined **시스템이나 js 엔진**이 값이 할당되지 않음을 우리에게 **알려주려고**
- Boolean
    - true/ false (대문자 쓰면 안됨)

### 자동 형변환

| 데이터 타입 | false 값 | true 값 |
| --- | --- | --- |
| undefined | 항상 false | X |
| null | 항상 false | X |
| Number | 0, -0, NaN | 나머지 모든 경우 |
| String | '' (빈 문자열) | 나머지 모든 경우 |

## 연산자

- 할당 연산자
    - 잘 됨
- 증가 & 감소 연산자
    - 증가 연산자 ++
    - 감소 연산자 —
        - ⇒ +=, -= 써라 그냥
- 비교 연산자 된다.
- 동등 연산자 ==
    - 두 피연산자가 같은 값으로 **평가**되는지 비교
        - 암묵적 타입 변환 적용되버림 ‘1’ == 1 ⇒ True
- 일치 연산자 ===
    - 두 피연산자의 **값**과 **차입** 둘 다 같아야 함
        - 0 === false ⇒ false
- 논리 연산자
    - and &&
    - or ||
    - not !
    - 단축 평가 지원 (and or 쓸 때 미리 순서대로 결과 때리는 거)

## 조건문

### if

- if (??== ‘값’) {

} else if (??==값) {

} else {
}

### 삼항 연산자

- condition
    - 평가할 조건 ( true 또는 fals로 평가)
- expression1
    - 조건 true반환
- expression2
    - 조건 false 반환

## 반복문

### while

: 조건문이 참이면 문장을 계속해서 수행

```jsx
while (조건문) {
	//do something
}
```

### for

: 특정한 조건이 거짓으로 판별될 때까지 반복

※증감문에 복합 할당 연산자 써야할 때도 있다.

※ ;(semi-colon) 반드시 붙여줘야 함

※ 초기문은 반드시 let을 써줘야 한다.

```jsx
for ([초기문]; [조건문]; [증감문]) {
	//do something
	}
```

### for … in, for … of

- for … in
    
    : 객체의 열거 가능한 속성에 대해 반복
    
    ※ const obj(객체)
    

```jsx
for (variable in object) {
	statement
}
```

- for … of
    
    : 반복 가능한 객체(배열, 문자열 등)에 대해 반복
    

```jsx
for (variable of iterable {
	statement
}
```

## 함수

### function

- **참조 자료형**에 속하며 모든 함수는 **Function** object
    
    ※ 참조 자료형 : 객체의 주소가 저장되는 자료형
    

### 함수 정의

- 함수 구조
    
    ```jsx
    function name ([param[,param,[..., param]]]) {
    	statements
    	return value
    }
    ```
    
- 2가지 표현 방법
    - 선언식 vs 표현식
- 함수 선언식 특
    - 호이스팅 됨
        
        ※ 호이스팅이란? 아직 선언되지 않은 함수인데, 호출이 되는 것
        
    - 구조나 가독성 면에서는 표현식에 비해 장점이 있음
- 함수 표현식 특
    - 호이스팅 안됨
    - 함수 이름이 없는 ‘익명 함수’를 사용할 수 있음
- why 표현식?
    1. 예측 가능성
    2. 유연성
    3. 스코프 관리

### 매개변수

1. 기본 함수 매개변수
    - 전달하는 인자가 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
2. 나머지 매개변수
    - 임의의 수의 인자를 ‘배열’로 혀용하여 가변 인자를 나타내는 방법
    
    ※ 작성 규칙
    
    - 함수 정의 시 나머지 매개변수는 하나만 작성 가능
    - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함
- 매개변수와 인자 개수 불일치 할 때
    - 누락 변수 → undefined
    - 초과 인자 제외

- Spread syntax (전개 구문)
    - 배열이나 문자열 같이 반복 가능 항목 펼치기 (확장, 전개)
    - 전개 대상에 따라 역할이 다름
        
        → 배열이나 객체의 요소를 개별적인 값으로 분리하거나, 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등
        

### 화살표 함수 표현식

: 함수 표현식의 간결한 표현법

- arrow function 사용 시
    - function, 괄호, 리턴, 중괄호 삭제 가능
    - function = ⇒ 대체
    - 매개 변수 괄호 삭제 (인자가 한 개 있을 때만 생략 가능)
    - {}, return 당연히 있을 거니까 빼기 (표현식이 한 줄 일 때만 {}, return 생략 가능)
- 최종 형태
    
    ```jsx
    const arrow2 = (name) => {return 'hello, ${name}'}
    ```
    

### 참고

- null vs undefined
    - null : 값이 없음
    - undefined : 값이 할당되지 않음