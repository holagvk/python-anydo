# -*- coding: utf-8 -*-
""" anydo.lib.error """


class AnyDoAPIBinderError(Exception):
    """An AnyDoAPIBinder error occured."""
    def __init__(self, msg):
        super(AnyDoAPIBinderError, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg
