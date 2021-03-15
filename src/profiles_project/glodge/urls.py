from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('lodge', views.LodgeDetailViewSet, base_name='lodge-viewset')

urlpatterns = [
    url(r'', include(router.urls)),
]
