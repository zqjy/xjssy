#!/usr/bin/env python
# encoding: utf-8

import xadmin
from apps.car.models import Carinfo, Carimageinfo


class CarinfoAdmin(object):
    list_display = ['CarId', 'CarName', 'ImageUrl', 'Load', 'LengthWidthHeight', 'CarType']


class CarimageinfoAdmin(object):
    list_display = ['CarImageId', 'CarId', 'ImageUrl', 'IsCover']


xadmin.site.register(Carinfo, CarinfoAdmin)
xadmin.site.register(Carimageinfo, CarimageinfoAdmin)
