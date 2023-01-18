from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'body', 'title_en', 'body_en')
