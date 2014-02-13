# -*- coding: utf-8 -*-
import base64
import uuid


def encode_string(value):
    return value.encode('utf-8') \
        if isinstance(value, unicode) else str(value)


def create_uuid():
    id = base64.b64encode(uuid.uuid4().bytes)
    safe_id = id.replace("+", "-").replace("/", "_")
    return safe_id
