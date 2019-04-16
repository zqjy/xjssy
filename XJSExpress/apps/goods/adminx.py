#!/usr/bin/env python
# encoding: utf-8

import xadmin
from apps.goods.models import GoodsInfo, GoodsImageInfo, GoodsCommentImageInfo, KmPriceInfo


class CustomerInfoAdmin(object):
    list_display = ['CustomerName', 'Gender', 'DateOfBirth', 'Mobile', 'WeiXinId', 'WeiXin', 'Point']

xadmin.site.register(GoodsInfo)
xadmin.site.register(GoodsImageInfo)
xadmin.site.register(GoodsCommentImageInfo)
xadmin.site.register(KmPriceInfo)


