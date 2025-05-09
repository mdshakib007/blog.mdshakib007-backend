from django.urls import path
from .views import BlogListView, RecentBlogListView, BlogDetailView, BlogClapView, BlogCommentCreateView, BlogCommentListView, BlogStatsView

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='blog-list'),
    path('recent-posts/', RecentBlogListView.as_view(), name='recent-blogs'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('posts/<int:pk>/clap/', BlogClapView.as_view(), name='blog-clap'),
    path('posts/<int:pk>/comments/add/', BlogCommentCreateView.as_view(), name='blog-comment-create'),
    path('posts/<int:pk>/comments/', BlogCommentListView.as_view(), name='blog-comment-list'),
    path('view/stats/', BlogStatsView.as_view(), name='stats'),
]