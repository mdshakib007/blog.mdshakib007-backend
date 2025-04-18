from rest_framework import serializers
from .models import Blog, Tag, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'body', 'created_at']
        read_only = ['id', 'created_at']


class BlogListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'tags', 'reads', 'clap_count', 'comment_count', 'created_at']


class BlogDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'image',
            'body', 'tags', 'reads', 
            'clap_count', 'created_at', 'updated_at',
        ]