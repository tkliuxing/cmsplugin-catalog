# -*- coding: utf-8 -*-
from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import ugettext_lazy as _

from .models import CatalogExtension


@toolbar_pool.register
class CatalogExtensionToolbar(ExtensionToolbar):
    # defineds the model for the current toolbar
    model = CatalogExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item url
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item
                current_page_menu.add_modal_item(
                    _('Catalog'), url=url, disabled=not self.toolbar.edit_mode)
