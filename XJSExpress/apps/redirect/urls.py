from django.conf.urls import url
from apps.redirect.views import RedirectViewSet
from apps.driver.views import CodeViewSet, DriverInfoViewSet
from rest_framework.routers import DefaultRouter

# 区域
get_area_info_list = RedirectViewSet.as_view({'post': 'get_area_info_list',})
get_area_info_model = RedirectViewSet.as_view({'post': 'get_area_info_model',})
# 车辆
get_car_info_list_json = RedirectViewSet.as_view({'post': 'get_car_info_list_json',})
get_apply_car_list = RedirectViewSet.as_view({'post': 'get_apply_car_list',})
get_car_info_model_json = RedirectViewSet.as_view({'post': 'get_car_info_model_json',})
# 司机
reg_code_info = CodeViewSet.as_view({'post': 'create',})
find_pwd_code_info = CodeViewSet.as_view({'post': 'find_pwd_code_info',})
reg_driver_info = DriverInfoViewSet.as_view({'post': 'create',})
edit_password = DriverInfoViewSet.as_view({'post': 'update_driver',})
login_driver_info = DriverInfoViewSet.as_view({'post': 'login_driver_info',})
exit_login = DriverInfoViewSet.as_view({'post': 'exit_login',})
get_driver_model = RedirectViewSet.as_view({'post': 'get_driver_model',})
driver_image_upLoad = DriverInfoViewSet.as_view({'post': 'driver_image_upLoad',})
apply_check_driver_info = DriverInfoViewSet.as_view({'post': 'apply_check_driver_info',})
edit_driver_info = DriverInfoViewSet.as_view({'post': 'edit_driver_info',})
get_order = RedirectViewSet.as_view({'post': 'get_order',})
get_cash = RedirectViewSet.as_view({'post': 'get_cash',})

urlpatterns = [
    url(r'^\s*GetAreaInfoJson', get_area_info_list, name='get_area_info_list'),  # 获取地区信息接口
    url(r'^\s*GetAreaInfoModel', get_area_info_model, name='get_area_info_model'),  # 获取单个地区信息接口
    url(r'^\s*GetCarInfoListJson', get_car_info_list_json, name='get_car_info_list'),  # 有参获取车辆列表对象
    url(r'^\s*GetApplyCarList', get_apply_car_list, name='get_apply_car_list'),  # 无参获取车辆列表对象
    url(r'^\s*GetCarInfoModelJson', get_car_info_model_json, name='get_car_info_model'),  # 获取某个车对象
    url(r'^\s*RegCodeInfo', reg_code_info, name='reg_code_info'),  # 生成注册码
    url(r'^\s*FindPwdCodeInfo', find_pwd_code_info, name='find_pwd_code_info'),  # 修改密码验证码
    url(r'^\s*RegDriverInfo', reg_driver_info, name='reg_driver_info'),  # 添加司机信息
    url(r'^\s*EditPassWord', edit_password, name='edit_password'),  # 找回密码
    url(r'^\s*LoginDriverInfo', login_driver_info, name='login_driver_info'),  # 司机登录
    url(r'^\s*ExitLogin', exit_login, name='exit_login'),  # 司机登录
    url(r'^\s*GetDriverInfoModelJson', get_driver_model, name='get_driver_model'),  # 获取单个司机
    url(r'^\s*DriverImageUpload', driver_image_upLoad, name='driver_image_upLoad'),  # 司机图片上传
    url(r'^\s*ApplyCheckDriverInfo', apply_check_driver_info, name='apply_check_driver_info'),  # 司机提交认证信息
    url(r'^\s*EditDriverInfo', edit_driver_info, name='edit_driver_info'),  # 司机个人信息修改
    url(r'^\s*Order', get_order, name='get_order'),  # 司机个人信息修改
    url(r'^\s*Cash', get_cash, name='get_cash'),  # 获取个人余额
]