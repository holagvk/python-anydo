# -*- coding: utf-8 -*-
import sys


def encode_string(value):
    if sys.version_info < (3, 0):
        return value.encode('utf-8') \
            if isinstance(value, unicode) else str(value)
    else:
        return value
