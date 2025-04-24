# DRF 02

### DRF with N:1 Relation

- 조회 (GET) (복수, 단일)
    - 기본적인 관계형 DB와 동일
- 추가 (POST)
    - 클라이언트로부터 입력 받지 않는 값(e.g. FK)의 경우 serializer 인스턴스를 저장하는 과정에서 추가 데이터를 받을 수 있음
        
        ```python
        serializer.save(FK키=FK키)
        ```
        
    - is_valid 단계에서 비어있는 FK키 에러를 처리하기 위해 **읽기 전용 필드** 활용
        - 읽기 전용 필드
            - 클라이언트가 데이터 생성 또는 수정 요청을 보낼 대 해당 필드에 값을 제공하거나 변경할 수 없으며, 서버가 응답 시에만 값을 표시하는 필드
            
            ※유효성 검사에 포함시키지 않고 응답 데이터에서는 빠짐
            
            - read_only_fields
            
            ※ 외래키를 직접 추가한 경우이니, 유효성 검사에서 제외
            
            - why 읽기 전용 필드?
                - 클라이언트 측에서 수정하면 안될 때
                - 서버 로직에 의해 자동 생성 관리 될 때
                - 입력은 받지 않지만 정보를 제공해야할 때
                - 새로운 필드 값을 만들어 제공해야 할 때
            
            ※생성 뿐 아니라 수정 때도 활용 됨
            
- 삭제(DELETE)
    - 동일
- 수정(PUT)
    - 동일

※ raise_exception = True

일반적이 404 응답으로 is_valid 단계에서 처리

- 응답 데이터 재구성
    - 댓글 조회 시 출력 내역 변경
        - e.g. article:  20(pk번호) → article : {title : “”} 아티클의 데이터로 overriding

### 역참조 데이터 구성

- Nested relationships (역참조 매니저 활용)
    - comment_set(역참조 매니저)를 재구성하기
    - comment_set을 override
- annotate 사용
    - view 함수에서 annotate를 활용해 새로운 속성 추가
    
    ```python
    from django.db.models import Count
    article= Article.objects.annotate(num_of_comments=Count('comment')).get(pk=article_pk)
    ```
    
- SerialIzerMethodField
    - 읽기 전용 필드 재구성 시 활용
    - DRR에서 제공하는 읽기 전용 필드
    - Serializer에서 추가적인 데이터 가공을 하고 싶을 때 사용
    
    ```python
    class UserSerializer(serializers.ModeSerializer):
    	<역참조 명칭> = serializers.SerializerMethodField()
    	class Meta:
    		...
    		
    		def get_<역참조 명칭>(self obj):
    			return obj.<역참조 매니저>
    ```
    

### API 문서화

- 대표적인 생성 Framework
    1. Swagger
    2. Redoc
- 두 개 동시에 설치 library
    - pip install drf-spectacular