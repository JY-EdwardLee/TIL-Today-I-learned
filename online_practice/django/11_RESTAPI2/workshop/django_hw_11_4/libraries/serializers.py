from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()

    class ReviewDetailSeiralizer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content', 'score',)

    review_set = ReviewDetailSeiralizer(many=True)

    def get_review_count(self, obj):
        return obj.review_count

    class Meta:
        model = Book
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class BookIsbnSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn',)
    
    book = BookIsbnSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('book',)