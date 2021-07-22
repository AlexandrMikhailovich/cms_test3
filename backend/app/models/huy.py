from django.db import models
from garpix_page.models import BasePage


class Huy(BasePage):
    content = models.TextField(verbose_name='Hyuuuu', blank=True, default='')

    template = 'pages/huy.html'

    class Meta:
        verbose_name = "Huy"
        verbose_name_plural = "huys"
        default_related_name = "huy_page"
        ordering = ('-created_at',)
