from django.db import models
from garpix_page.models import BasePage


class Post(BasePage):
    content = models.TextField(verbose_name='Content', blank=True, default='', )

    template = 'pages/post.html'

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        default_related_name = "Content_post"
        ordering = ('-created_at',)
