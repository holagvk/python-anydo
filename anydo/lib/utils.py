# -*- coding: utf-8 -*-
""" anydo.lib.utils """
import sys
import base64
import uuid


def encode_string(value):
    """ encoding string
    Returns: value | utf-8 encoded string
    :param value: utf-8 encoded string or unicode
    """
    if sys.version_info < (3, 0):
        return value.encode('utf-8') \
            if isinstance(value, unicode) else str(value)
    else:
        return value


def create_uuid():
    """ creating uuid.
    Returns: utf-8 encoded and base64 encoded uuid that is as follows;
             e.g. u'08s-gOkKSWC26ntWUGkKIQ=='
    """
    unique_id = base64.b64encode(uuid.uuid4().bytes)
    safe_id = unique_id.replace(b"+", b"-").replace(b"/", b"_")
    return safe_id.decode('utf-8')
