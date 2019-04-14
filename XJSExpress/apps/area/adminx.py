#!/usr/bin/env python
# encoding: utf-8

import xadmin
from apps.area.models import Areainfo


class AreainfoAdmin(object):
    list_display = ['AreaId', 'AreaName', "ParentId"]


xadmin.site.register(Areainfo, AreainfoAdmin)
