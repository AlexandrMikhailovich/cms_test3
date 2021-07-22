from modeltranslation.translator import TranslationOptions, register
from ..models import Huy


@register(Huy)
class HuyTranslationOptions(TranslationOptions):
    fields = ('content',)
