from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    author = models.CharField(max_length=34, verbose_name=_('author'))
    image_cover = models.ImageField(verbose_name=_('image cover'), help_text=_('recommended: Image(420X260)'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(750X450)'))
    date = models.DateTimeField(default=timezone.now(), verbose_name=_('date'))
    body = RichTextField(verbose_name=_('body'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
