from django.conf.urls import url, include
from apps.area.views import AreaListViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'list', AreaListViewSet, base_name='list')

retrieve_by_name = AreaListViewSet.as_view({'get': 'retrieve_by_name',})


urlpatterns = [
    url(r'^list/(?P<area_name>\w+)', retrieve_by_name, name='retrieve_by_name'),
    url(r'^', include(router.urls)),  # Router 方式
]