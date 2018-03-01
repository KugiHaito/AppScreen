"""AppScreen Documentation.

AppScreen is a desktop application manager, using the
Kivy graphical user interface (GUI). Enabling agile
and effective creation and development

For other examples of creating and using layouts in this module,
read the documentation:

on `Github <http://github.com/KugiHaito/AppScreen>`_

----

AppScreen has a modular design, consisting of a few subpackages, which can
also be used by themselves:
* flexx.core - the configures
* flexx.layout - the templates
* flexx.manager - the handle templates or sheet
* flexx.sheets - the util sheets

"""
import os
import sys

__version__ = '0.6.1-dev'

if sys.version_info < (3, 6):
    raise RuntimeError('AppScreen needs at least Python 3.6')
else:
    sub_modules = [f for f in os.walk('appscreen/')]

    for module, _, f in sub_modules:
        x = 0
        module = module.replace('appscreen/', '')
        if '__pycache__' not in module:
            while(x < len(module)):
                module = module.replace('/', '.').replace('\\', '.')
                exec("from .{} import *".format(module))
                x += 1
