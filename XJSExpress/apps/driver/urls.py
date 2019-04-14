from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.driver.views import CodeViewSet, DriverInfoViewSet


router = DefaultRouter()
# router.register(r'code', CodeViewSet, base_name='code')
# router.register(r'info', DriverInfoViewSet, base_name='info')
get_driver_model = DriverInfoViewSet.as_view({'get':'retrieve'})  # 获取某个司机信息
urlpatterns = [
    url(r'^get_driver_model/(?P<pk>\d+)', get_driver_model, name='get_driver_model'),
    url(r'^', include(router.urls)),  # Router 方式
]