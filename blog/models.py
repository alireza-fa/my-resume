from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from utils.managers import IsActiveManager


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    title_en = models.CharField(max_length=120, verbose_name=_('title english'))
    author = models.CharField(max_length=34, verbose_name=_('author'))
    author_en = models.CharField(max_length=34, verbose_name=_('author'))
    image_cover = models.ImageField(verbose_name=_('image cover'), help_text=_('recommended: Image(420X260)'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(750X450)'))
    date = models.DateTimeField(default=timezone.now(), verbose_name=_('date'))
    body = RichTextField(verbose_name=_('body'))
    body_en = RichTextField(verbose_name=_('body english'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    @classmethod
    def get_posts_two_part(cls):
        posts = cls.objects.all()
        posts_count = posts.count()
        posts_half_count = round(posts_count / 2)
        post_part_one = posts[:posts_half_count]
        post_part_two = posts[posts_half_count:]
        post_part = [post_part_one, post_part_two]
        return post_part


class NewsletterSubscribe(models.Model):
    email = models.EmailField(max_length=120, verbose_name=_('email'))

    class Meta:
        verbose_name = _('Newsletter Subscribe')
        verbose_name_plural = _('Newsletters Subscribes')

    def __str__(self):
        return self.email
