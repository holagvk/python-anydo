# -*- coding: utf-8 -*-


def encode_string(value):
    return value.encode('utf-8') \
        if isinstance(value, unicode) else str(value)
