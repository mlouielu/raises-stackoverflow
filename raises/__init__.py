# -*- coding: utf-8 -*-
"""When Python raises, we Stack Overflow
"""

__version__ = '0.1'


import sys
import webbrowser

# Compatibility for Python 2 and 3
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


STACKOVERFLOW_URL = 'https://stackoverflow.com/search?tab=votes&{qs}'


def raiser(etype, value, tb):
    error_msg = '{etype}: {value}'.format(etype=etype.__name__, value=value)
    webbrowser.open(STACKOVERFLOW_URL.format(
        qs=urlencode({'q': '[python] ' + error_msg})), new=2)  # new=2 open in new tab

    # sys.__excepthook__ is the original excepthook, perform to print traceback
    # See https://docs.python.org/3/library/sys.html#sys.__excepthook__
    sys.__excepthook__(etype, value, tb)


# Globaly replace sys.excepthook to raiser
sys.excepthook = raiser
