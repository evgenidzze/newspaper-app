from django.contrib import admin

from articles.models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']


admin.site.register(Articles, ArticlesAdmin)
