=================
cmsplugin-catalog
=================

|ci| |pypi| |status|

.. |ci| image:: https://travis-ci.org/tkliuxing/cmsplugin-catalog.png?branch=master
    :target: https://travis-ci.org/tkliuxing/cmsplugin-catalog

.. |pypi| image:: https://pypip.in/version/cmsplugin-catalog/badge.png?text=pypi
    :target: https://pypi.python.org/pypi/cmsplugin-catalog/
    :alt: Latest Version

.. |status| image:: https://pypip.in/status/cmsplugin-catalog/badge.png
    :target: https://pypi.python.org/pypi/cmsplugin-catalog/
    :alt: Development Status


May you want insert a pages list tree.
This Django CMS plugin allows you to add pages list to the page.

Requirements
============

It works fine and tested under ``Python 2.7``. The following libraries are required

- ``Django`` >= 1.5
- ``django-cms`` >= 3.0, <3.1 (we recommend to use Django CMS 3.0 and higher, lower than 3.1, contact us if you need prior CMS versions supports and have some issues)

Installation
============

::

$ pip install cmsplugin-catalog

Configure installed apps in your ``settings.py`` ::

  INSTALLED_APPS = [
      # django contrib and django cms apps
      'cmsplugin_catalog',
  ]

Migrate your database ::

  django-admin.py migrate cmsplugin_catalog

Usage
=====

Add plugin to the page with common way. 
To customize how it looks you can override `cms/plugins/catalog_list_panel.html`.

Roadmap
=======
- Python 3 support

Changelog
=========
The changelog can be found at `repo's release notes <https://github.com/tkliuxing/cmsplugin-catalog/releases>`_

Contributing
============
Fork the repo, create a feature branch then send me pull request. Feel free to create new issues or contact me via email.

Translation
-----------
You could also help me to translate `cmsplugin-catalog` to your native language `with Transifex <https://www.transifex.com/projects/p/cmsplugin-catalog/resource/core/>`_