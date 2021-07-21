from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "каталог"

# Create your models here.
