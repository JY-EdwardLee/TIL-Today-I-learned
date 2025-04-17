from rest_framework import serializers
from .models import Article, Comment


# 게시글의 일부 필드를 직렬화 하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # 새로운 필드 생성
    num_of_comments = serializers.SerializerMethodField()

    # 기존에 있던 역참조 매니저의 값을 덮어쓰기
    comment_set = CommentDetailSerializer(read_only=True, many=True)
    # comments = CommentDetailSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = '__all__'

    # SerializerMethodField의 값을 채울 함수 (이름 형식 get_<SMF의 필드명>으로 맞춰줘야 동작함)
    def get_num_of_comments(self, obj):
        # annotate가 어려울 땐 아래처럼 직접 검색 가능
        obj.comment_set.count()
        # 여기서 obj는 특정 게시글 instance
        # view 함수에서 annotate 해서 생긴 새로운 속성(num_of_comments)을 사용할 수 있게됨
        return obj.num_of_comments


# 댓글에 전체 필드를 직렬화 하는 클래스
class CommentSerializer(serializers.ModelSerializer):
    # 응답 데이터 중 aricle 데이터를 재구성하기 위한 클래스 만들기
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 외래 키 필드인 article의 데이터를 재구성
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 외래키 필드를 유효성 검사 목록에서 빼줘야 함
        # 왜 why? 외래키를 외부에서 받지 않고 우리가 직접 넣었기 때문에
        # read_only_fields = ('article',)