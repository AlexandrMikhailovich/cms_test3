from garpixcms.urls import *  # noqa
from rest_framework.routers import DefaultRouter
from .views import PageApiView

router = DefaultRouter()
urlpatterns = [
                path('', include('catalog.urls')),
                re_path(r'page_api/', PageApiView.as_view(),)

              ] + urlpatterns  # noqa
