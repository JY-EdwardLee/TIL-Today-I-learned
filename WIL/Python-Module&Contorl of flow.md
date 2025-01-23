# Modules & Control of flow

## 모듈(Modules)

- 한 파일로 묶인 **변수**와 **함수**의 모음, **특정한 기능을 하는 코드**가 작성된 파이썬 파일(.py)
    - why 모듈?
        
        : 다른 프로그래머가 이미 작성해 놓은 코드를 활용하기 위해
        
    - e.g. math 내장 모듈
        - 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
        
        ```python
        import math
        import random
        import datetime
        
        print(math.pi) #3.14159265358993 <- 함수X 변수임
        print(math.sqrt(4)) #2.0 <- 함수O
        
        random.seed(99)
        print(random.randint(1,10))
        
        now = datetime.datetime.now()
        print(now)
        ```
        
        ※ 파이썬 파일 내에 math.py, random.py, datetime.py 파일이 존재
        
    - 모듈 사용하기
        - import 문, from 절
            - import 모듈 (✅ 권장됨)
            - from 모듈 import 함수
                
                ⇒ 모듈을 가져오지 않았기에, .(dot)앞에 모듈명을 쓸 필요 없음
                
        - ‘.(dot)’ 연산자
            
            : 점의 왼쪽 객체에서 오른쪽 이름을 찾아라
            
        - ‘as’ 키워드
            
            : 별칭을 부여 → 동일한 이름 변수, 함수, 글래스 등을 가져올 때 발생하는 이름 충돌 해결
            
    - 모듈 주의사항
        - 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
            
            ⇒ 마지막에 import된 이름으로 대체됨
            
        - from 모듈 import * ← 권장하지 않음
    - 직접 정의한 모듈 사용하기

### 파이썬 표준 라이브러리 (PSL)

- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
    
    ※ 별도의 설치 없이 import 가능
    
    - 라이브러리
        
        : 연관된 모듈과 패키지들을 디렉토리에 모아 놓은 것
        
    - 패키지
        
        : 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것
        

```python
import library
import package

from library.package import module
from package import module
```

### 외부패키지

- pip를  사용하여 설치 후 import 가능
    - 외부패키지 사용법 : pip install package명 ⇒ 설치

---

## 제어문

- 코드의 실행 흐름을 제어하는 데 사용되는 구문, **조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행

### 조건문

- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

**if statement**

- if / elif / else
- 표현법
    
    ```python
    if 표현식: # 단독 사용 가능
    	if 표현식: # 중첩 조건
    		코드 블록
    elif 표현식: # 선택적, 복수 조건문
    	코드 블록
    else:
    	코드 블록
    ```
    

### 반복문

- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- for, while
- 반복문 제어
    - break, continue, pass

**for statement**

: 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

- for문 기본 구조

```python
for 변수 in *iterable: #iterable = 반복 가능한 객체 (e.g. dict, set 포함)
	코드 블록
```

- for 문 작동원리
    - 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
    - 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행
    - 마지막을 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
- 순회
    - 문자열 순회
    - range 순회
    - dict 순회
        
        ※ 인덱스 번호는 없으나, 작성한 순서대로 순회
        
    - 인덱스로 리스트 순회
    
    ```python
    numbers = [4, 12, 4, 3, -1]
    
    for i in range(len(numbers)):
    	numbers[i] = numbers[i] * 2
    
    print(numbers)
    ```
    
- 중첩된 반복문
    
    ```python
    outers = ['A', 'B']
    inners = ['C', 'D']
    
    for outer in outers:
    	for inner in inners:
    		print(outer, inner)
    ```
    

**while statement**

: 주어진 조건식이 참인 동안 코드를 반복해서 실행 == 조건식이 거짓이 될 때 까지 반복

- while문 기본구조
    
    ```python
    while 조건식:
    	코드 블록
    ```
    

### 반복 제어

- break / continue / pass
    - break : 반복을 즉시 중지
        
        ```python
        number = int(input('양의 정수를 입력해주세요.: '))
        while number <= 0:
            if number == -9999:
                print('프로그램을 종료합니다.')
                break
            if number < 0:
                print('음수를 입력했습니다.')
            else:
                print('0은 양의 정수가 아닙니다.')
            number = int(input('양의 정수를 입력해주세요.: '))
        print('잘했습니다!')
        ```
        
        ※ 플래그 변수 : **플래그 변수**란 특정 조건의 참(`True`) 또는 거짓(`False`) 상태를 저장하여 프로그램의 흐름을 제어하거나 어떤 상태를 나타내는 데 사용되는 변수
        
    - continue : 다음 반복으로 건너뜀
        
        ```python
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        for i in numbers:
            if i % 2 == 0:
                continue
            print(i)
        ```
        
    - pass : 아무 작업도 안함
        - why pass?
            
            : 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생할 수 있음
            
            : 조건문에서 아무런 동작을 주행하지 않아야 할 때
            
            : 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법
            

---

## 참고

### List Comprehension 구조

- 간결하고 효율적인 리스트 생성 방법
- List Comprehension 구조
    
    ```python
    [expression for 변수 in iterable]
    [expression for 변수 in iterable if 조건식]
    ```
    
    **※ Comprehension을 남용하지 말자**
    

### 모듈 내부 살펴보기

- help(module명)

### enumerate

- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

---

### 참고

- for statement
    - for else (flag 변수 대체)
        - else 동작 조건
            - 중간에 break로 탈출하지 않고, loop를 끝까지 돌았을 때 동작
        - 사용법
            
            ```python
            for i in range(10):
            	if i == 5:
            		break
            else:
            	print("이것이 for as 문법이다")
            ```
            
    - flag 변수 사용 시
        
        ```python
        flag = False
        for i in range(10):
        	if i == 5:
        		print("5번째에")
        		flag = Ture
        		break
        if not flat:
        	print("전부돌")
        ```