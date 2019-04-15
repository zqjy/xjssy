#!/usr/bin/env python
# encoding: utf-8

import xadmin
from apps.customer.models import CustomerInfo, CustomerAccountInfo, CustomerAccountDetailsInfo


class CustomerInfoAdmin(object):
    list_display = ['CustomerName', 'Gender', 'DateOfBirth', 'Mobile', 'WeiXinId', 'WeiXin', 'Point']

xadmin.site.register(CustomerInfo, CustomerInfoAdmin)
xadmin.site.register(CustomerAccountInfo)
xadmin.site.register(CustomerAccountDetailsInfo)


