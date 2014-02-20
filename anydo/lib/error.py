# -*- coding: utf-8 -*-
class AnyDoClientError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class AnyDoClientError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return "(%s): %s" % (self.code, self.msg)
