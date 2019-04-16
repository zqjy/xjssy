"""XJSExpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from XJSExpress.settings import MEDIA_ROOT
from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 用户登录测试配置
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 访问本地文件
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 文档
    url(r'docs/', include_docs_urls(title='小样工程')),
    # drf自带的用户认证返回token
    url(r'^api_token_auth/', views.obtain_auth_token),
    # jwt认证接口
    url(r'^jwt_auth/', obtain_jwt_token),
    # 文档接口
    url(r'^H5Driver/', include('apps.redirect.urls', namespace='redirect')),
    # 区域
    url(r'^area/', include('apps.area.urls', namespace='area')),
    # 车辆
    url(r'^car/', include('apps.car.urls', namespace='car')),
    # 司机
    url(r'^driver/', include('apps.driver.urls', namespace='driver')),
    # 货单
    url(r'^goods/', include('apps.goods.urls', namespace='goods')),
    # 顾客
    url(r'^customer/', include('apps.customer.urls', namespace='customer')),

]
