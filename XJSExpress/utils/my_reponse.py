# coding=utf-8
from collections import OrderedDict
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict


def get_response_dict(data='', msg=''):
    """
    添加返回数据字段
    :param data:
    :return:
    """
    dict = OrderedDict()
    dict["Code"] = 1
    if not msg:
        dict["Msg"] = "获取成功"
    else:
        dict["Msg"] = msg
    dict["Success"] = True
    list = []
    if isinstance(data, ReturnList):  # 数据列表
        dict["Data"] = data
    elif isinstance(data, ReturnDict):  # 详细信息
        list.append(data)
        dict["Data"] = list
    elif isinstance(data, str):  #
        dict["Data"] = data
    else:
        list.append(data)
        dict["Data"] = list
    return dict

def get_response_error_dict(msg=''):
    """
    添加返回错误提示
    :return:
    """
    dict = OrderedDict()
    dict["Code"] = 2
    if not msg:
        dict["Msg"] = "参数异常"
    else:
        dict["Msg"] = msg
    dict["Sussess"] = False
    dict["Data"] = None
    return dict
