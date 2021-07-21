from django.db import models
from garpix_page.models import BasePage


class Page(BasePage):
    content = models.TextField(verbose_name='Content', blank=True, default='')

    template = 'pages/default.html'

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        default_related_name = "Content_page"
        ordering = ('-created_at',)
