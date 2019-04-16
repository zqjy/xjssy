from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.customer.views import CustomerInfoViewSet


router = DefaultRouter()
router.register(r'info', CustomerInfoViewSet, base_name='info')
customer_update = CustomerInfoViewSet.as_view({'post': 'update'})
urlpatterns = [
    url(r'^update/(?P<pk>\d+)', customer_update, name='customer_update'),  # 个人信息修改
    url(r'^', include(router.urls)),  # Router 方式
]