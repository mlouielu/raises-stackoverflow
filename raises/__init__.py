# -*- coding: utf-8 -*-
"""Raises' in your source code, all's right with the Stack Overflow
"""

__version__ = '0.2'


import sys
import webbrowser

# Compatibility for Python 2 and 3
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


STACKOVERFLOW_URL = 'https://stackoverflow.com/search?tab=votes&{qs}'
__enabled = True


def raiser(etype, value, tb):
    if __enabled:
        error_msg = '{etype}: {value}'.format(etype=etype.__name__, value=value)
        webbrowser.open(STACKOVERFLOW_URL.format(
            qs=urlencode({'q': '[python] ' + error_msg})), new=2)  # new=2 open in new tab

    # sys.__excepthook__ is the original excepthook, perform to print traceback
    # See https://docs.python.org/3/library/sys.html#sys.__excepthook__
    sys.__excepthook__(etype, value, tb)


def disable():
    global __enabled
    __enabled = False


def enable():
    global __enabled
    __enabled = True


# Globaly replace sys.excepthook to raiser
sys.excepthook = raiser
