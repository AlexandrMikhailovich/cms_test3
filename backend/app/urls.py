from garpixcms.urls import *  # noqa
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
urlpatterns = [
                  path('', include('catalog.urls'))
              ] + urlpatterns  # noqa
