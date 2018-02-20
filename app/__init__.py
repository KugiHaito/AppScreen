# -*- coding: utf-8 -*-
"""Documentation.

AppLogin is a free code application, created for learning purposes and free use
that uses Graphical User Interface(GUI) Kivy for better handling.

You can use AppLogin to access, and manage data in a simple way.

the code is on `Github <http://github.com/KugiHaito/AppLogin>`
"""

__appname__ = 'AppLogin'
__author__ = 'Kugi Haito'
__version__ = '0.1.8-dev'

# Assert compatibility and redirect to legacy version on Python 2.7
import sys
ok = True

if sys.version_info[0] == 2:  # pragma: no cover
    if sys.version_info < (2, 7):
        raise RuntimeError(__appname__+' needs at least Python 2.7')
    if type(b'') == type(''):  # noqa - will be str and unicode after conversion
        sys.modules[__name__] = __import__(__name__ + '_legacy')
        ok = False

# Import config object
if ok:
    from ._config import config  # noqa
    from .util.logging import set_log_level  # noqa
    set_log_level(config.log_level)

del sys, ok
