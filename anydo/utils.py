# -*- coding: utf-8 -*-
import sys
import base64
import uuid


def encode_string(value):
    if sys.version_info < (3, 0):
        return value.encode('utf-8') \
            if isinstance(value, unicode) else str(value)
    else:
        return value


def create_uuid():
    id = base64.b64encode(uuid.uuid4().bytes)
    safe_id = id.replace("+", "-").replace("/", "_")
    return safe_id
