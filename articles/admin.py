from django.contrib import admin

from articles.models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']
    inlines = [CommentInline]


admin.site.register(Article, ArticlesAdmin)
admin.site.register(Comment)
