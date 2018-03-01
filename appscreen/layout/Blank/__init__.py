"""Blank Documentation.

This is a template blank, ready for use
"""
import os

modules = [f for f in os.walk('appscreen/layout/Blank')]

for _, _, module in modules:
    x = 0
    while(x < len(module)):
        m = module[x].split('.')
        if m[1] == 'py' and not m[0] == '__init__':
            exec("from .{} import {}".format(m[0], m[0]))
        x += 1
