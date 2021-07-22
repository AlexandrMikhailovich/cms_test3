from ..models.huy import Huy
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(Huy)
class HuyAdmin(BasePageAdmin):
    pass
