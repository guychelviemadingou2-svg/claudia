from django.contrib import admin

from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    autocomplete_fields = ('author', 'likes')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_at', 'parent')
    search_fields = ('body',)
    list_filter = ('created_at',)
    autocomplete_fields = ('author', 'article', 'parent')
