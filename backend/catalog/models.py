from django.db import models
from garpix_page.models import BasePage


class Catalog(BasePage):
    body = models.CharField(max_length=100, blank=True)
    content = models.TextField(verbose_name='Catalog', blank=True, default='')

    template = 'pages/catalog.html'

    # def get_context(self, request=None, *args, **kwargs):
    #     super(Catalog, self).get_context(**kwargs)
    #     PRODICTS = Producrt.AC...(CATEGORY=SELF)
    #     context.update(
    #         {
    #             'PRODICTS': PRODICTS
    #         }
    #     )
    #     return context

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalog"
        default_related_name = "Catalog"
        ordering = ('-created_at',)
