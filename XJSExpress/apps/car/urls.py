from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.car.views import CarListViewSet


router = DefaultRouter()
router.register(r'list', CarListViewSet, base_name='list')

urlpatterns = [
    url(r'^', include(router.urls)),  # Router 方式
]