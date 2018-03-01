"""Sheets Documentation.

Submodule in charge of managing supplies for layouts and other submodules
"""
import os

modules = [f for f in os.walk('appscreen/sheets')]

for _, _, module in modules:
    x = 0
    while(x < len(module)):
        m = module[x].split('.')
        if m[1] == 'py' and not m[0] == '__init__':
            exec("from .{} import *".format(m[0]))
        x += 1
