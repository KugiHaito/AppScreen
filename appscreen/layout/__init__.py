"""Layout Documentation.

This is a pack of templates, ready for use
"""

import os

modules = [f for f in os.walk('appscreen/layout/')]

for module, _, f in modules:
    x = 0
    module = module.replace('appscreen/layout/', '')
    if '__pycache__' not in module:
        while(x < len(module)):
            exec("from .{} import *".format(module))
            x += 1
