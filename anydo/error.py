# -*- coding: utf-8 -*-
""" anydo.error """

class AnyDoAPIError(Exception):
    """An AnyDoAPI error occured."""
    def __init__(self, code, msg):
        super(AnyDoAPIError, self).__init__(code, msg)
        self.code = code
        self.msg = msg

    def __str__(self):
        return "(%s): %s" % (self.code, self.msg)
