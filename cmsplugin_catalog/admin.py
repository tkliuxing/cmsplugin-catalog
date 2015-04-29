# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.extensions import PageExtensionAdmin, TitleExtensionAdmin

from .models import CatalogExtension


class CatalogExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(CatalogExtension, CatalogExtensionAdmin)