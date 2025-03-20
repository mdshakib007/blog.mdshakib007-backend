from django.contrib import admin
from .models import Tag, Blog, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'clap_count', 'is_published', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'body']
    ordering = ['-created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'name', 'short_body', 'created_at']
    list_display_links = ['id', 'blog']
    list_filter = ['created_at']
    search_fields = ['name', 'body']
    ordering = ['-created_at']

    def short_body(self, obj):
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body
    short_body.short_description = "Comment"


admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)