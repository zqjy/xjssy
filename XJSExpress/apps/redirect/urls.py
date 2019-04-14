from django.conf.urls import url
from apps.redirect.views import RedirectViewSet
from apps.driver.views import CodeViewSet, DriverInfoViewSet
from rest_framework.routers import DefaultRouter

# 区域
get_area_info_list = RedirectViewSet.as_view({'post': 'get_area_info_list',})
get_area_info_model = RedirectViewSet.as_view({'post': 'get_area_info_model',})
# 车辆
get_car_info_list_json = RedirectViewSet.as_view({'post': 'get_car_info_list_json',})
get_car_info_model_json = RedirectViewSet.as_view({'post': 'get_car_info_model_json',})
# 司机
reg_code_info = CodeViewSet.as_view({'post': 'create',})
find_pwd_code_info = CodeViewSet.as_view({'post': 'find_pwd_code_info',})
reg_driver_info = DriverInfoViewSet.as_view({'post': 'create',})
edit_password = DriverInfoViewSet.as_view({'post': 'update_driver',})
login_driver_info = DriverInfoViewSet.as_view({'post': 'login_driver_info',})
get_driver_model = RedirectViewSet.as_view({'post': 'get_driver_model',})

urlpatterns = [
    url(r'^\s*GetAreaInfoJson', get_area_info_list, name='get_area_info_list'),  # 获取地区信息接口
    url(r'^\s*GetAreaInfoModel', get_area_info_model, name='get_area_info_model'),  # 获取单个地区信息接口
    url(r'^\s*GetCarInfoListJson', get_car_info_list_json, name='get_car_info_list'),  # 获取车辆列表对象
    url(r'^\s*GetCarInfoModelJson', get_car_info_model_json, name='get_car_info_model'),  # 获取某个车对象
    url(r'^\s*RegCodeInfo', reg_code_info, name='reg_code_info'),  # 生成注册码
    url(r'^\s*FindPwdCodeInfo', find_pwd_code_info, name='find_pwd_code_info'),  # 修改密码验证码
    url(r'^\s*RegDriverInfo', reg_driver_info, name='reg_driver_info'),  # 添加司机信息
    url(r'^\s*EditPassWord', edit_password, name='edit_password'),  # 添加司机信息
    url(r'^\s*LoginDriverInfo', login_driver_info, name='login_driver_info'),  # 司机登录
    url(r'^\s*GetDriverInfoModelJson', get_driver_model, name='get_driver_model'),  # 司机登录
]