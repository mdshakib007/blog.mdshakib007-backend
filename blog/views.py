from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count, Prefetch, F, Sum
from django.http import Http404
from .models import Blog, Tag, Comment
from .serializers import BlogListSerializer, BlogDetailSerializer, CommentSerializer, TagSerializer


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class BlogListView(generics.ListAPIView):
    serializer_class = BlogListSerializer
    pagination_class = BlogPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        return (
            Blog.objects.filter(is_published=True)
            .prefetch_related('tags')
            .annotate(comment_count=Count('comments'))
            .order_by('-created_at')
        )


class RecentBlogListView(generics.ListAPIView):
    serializer_class = BlogListSerializer

    def get_queryset(self):
        return (
            Blog.objects.filter(is_published=True)
            .prefetch_related('tags')
            .annotate(comment_count=Count('comments'))
            .order_by('-created_at')[:3]
        )


class BlogDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            blog = Blog.objects.filter(is_published=True).prefetch_related('tags').get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        Blog.objects.filter(pk=blog.pk).update(reads=F('reads') + 1)
        blog.refresh_from_db()
        
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogClapView(APIView):
    def post(self, request, pk, format=None):
        try:
            blog = Blog.objects.get(pk=pk, is_published=True)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
        Blog.objects.filter(pk=blog.pk).update(clap_count=F('clap_count') + 1)
        blog.refresh_from_db()
        
        return Response({"clap_count": blog.clap_count}, status=status.HTTP_200_OK)


class BlogCommentCreateView(APIView):
    def post(self, request, pk, format=None):
        try:
            blog = Blog.objects.get(pk=pk, is_published=True)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = BlogPagination  # Use the same pagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(blog_id=pk).order_by('-created_at')


class BlogStatsView(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(is_published=True)

        total_blogs = blogs.count()
        total_views = blogs.aggregate(total_reads=Sum('reads'))['total_reads'] or 0
        total_claps = blogs.aggregate(total_claps=Sum('clap_count'))['total_claps'] or 0
        total_comments = Comment.objects.count()
        impression_prediction = total_views * 9  # or 8

        return Response({
            "total_blogs": total_blogs,
            "total_views": total_views,
            "total_claps": total_claps,
            "total_comments": total_comments,
            "impression_prediction": impression_prediction
        }, status=status.HTTP_200_OK)