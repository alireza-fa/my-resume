from django.contrib import admin

from blog.models import Post, NewsletterSubscribe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'body', 'title_en', 'body_en')


@admin.register(NewsletterSubscribe)
class NewsletterSubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
