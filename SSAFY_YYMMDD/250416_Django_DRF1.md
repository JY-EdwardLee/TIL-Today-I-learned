# DRF 01

## REST API

### API (Application Programming Interface)

: 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘

⇒ 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

- why API?
    - 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공
- Web API
    - 웹 서버 또는 웹 브라우저를 위한 API
        - 직접 개발하기 보다는 여러 Open API 들을 활용하는 추세

### REST (Representational State Transfer)

: API Server를 개발하기 위한 일종의 소프트웨어 설계 **방법론** **(규칙은 아닙니다.)**

⇒ API Server를 설계하는 구조가 서로 다르니 이렇게 맞춰서 설계하는 게 어떻겠는가?

- RESTful API
    - RESTful : REST원리를 따르다
    - **자원을 정의**하고 **자원에 대한 주소를 지정**하는 전반적인 방법을 서술

### REST API

: REST라는 설계 디자인 약속을 지켜 구현한 API

- 자원을 정의하고 주소를 지정하는 방법
    1. 자원의 **식별**
        - URI
    2. 자원의 **행위**
        - HTTP Methods (e.g. post, get …)
    3. 자원의 **표현** (어떻게 응답할 것인가?)
        - JSON 데이터
            
            (궁극적으로 표현되는 데이터 결과물)
            
- **URI (자원의 식별)**
    
    : 인터넷에서 리소스(자원)를 식별하는 문자열
    
    ⇒ 가장 일반적인 URI는 URL이다.
    
    - URL
        
        : 웹에서 주어진 리소스의 주소 ⇒ 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속
        

```jsx
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument
│     │                │   │                    │                       │
│     │                │   │                    │                       └── Anchor (Fragment)
│     │                │   │                    └───────── Parameters (Query String)
│     │                │   └──────────── Path (to the file/resource)
│     │                └──────────── Port
│     └─────────────────────────── Domain Name
└───────────────────────────────── Scheme (Protocol)
# http : 스킴(Scheme) – 사용하는 프로토콜 (ex. http, https, ftp 등)

# www.example.com : 도메인(Domain) – 서버 주소

# :80 : 포트 번호 – 서버의 접속 포트 (기본값일 경우 생략 가능: http는 80, https는 443)
	# 사실 :8000은 80 포트의 00번이다

# /path/to/myfile.html : 경로(Path) – 서버 내의 자원 위치
	# 요즈음은 실제 위치가 아닌 추상화된 형태의 구조로 표현

# ?key1=value1&key2=value2 : 쿼리 문자열(Query Params) – 요청에 대한 추가 정보
	# GET 방식으로 보낼 때 활용

# #SomewhereInTheDocument : 앵커(Anchor) – 문서 내 특정 위치로 이동
	# #(fragment identifier)이하는 서버로 전달 되지는 않음
```

- **HTTP Request Methods (자원의 행위)**
    
    : 리소스에 대한 행위(수행하고자 하는 동작)를 정의
    
    ⇒ HTTP verbs라고도 함
    
    - 4가지 대표 Method
        1. GET
            - 서버에 리소스의 표현을 요청
        2. POST
            - 데이터를 지정된 리소스에 제출
        3. PUT
            - 요청한 주소의 리소스를 수정
        4. DELETE
            - 지정된 리소스를 삭제
    - HTTP response status codes
        
        : 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
        
        - 5가지 응답 그룹으로 분류됨
- **자원의 표현**
    
    : REST API는 **JSON 타입**으로 응답하는 것을 권장
    
    - 이제부터는 Django에서 JSON 데이터를 응답하고, 그 데이터를 받아서 Front-end Framework를 그림

## DRF with Single Model

### Django REST framework

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
    
    ※ 설치 해야함
    
    ```bash
    pip install djangorestframework
    ```
    
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
    ```
    

## CRUD with ModelSerializer

### Serialization (직렬화)

: 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정 

⇒ 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

(e.g. querySet 형식은 크롬에서 이해할 수 없다)

- Serializer
    - Serialization하기 위해 필요한 클래스
    - Serialized data를 반환하는 클래스
- ModelSerializer
    - Django 모델과 연결된 Serializer 클래스
        
        ⇒ 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 Serialization을 진행
        
    
    ※ 다수데이터 명명 시 클래스명에 List 붙이기
    
    - ModelForm의 구조와 유사한 형식

- 앞으로는 Method를 기반으로 CRUD 진행 가능
    - url → view 순서로 작성 (templates 빠짐)
- **api_view** decorator
    - view함수를 실행하기전에 HTTP Method를 확인해서 허용하는 method만 통과
        
        ※ default로 GET은 포함됨