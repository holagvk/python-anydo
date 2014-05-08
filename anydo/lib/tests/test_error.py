# -*- coding: utf-8 -*-

import unittest
from anydo import error
from anydo.lib import error as lib_error


class ErrorTests(unittest.TestCase):

    def test_error_msg(self):
        self.assertEqual(error.AnyDoAPIError('dummy', 'test').__str__(),
                         '(dummy): test')

    def test_lib_error_msg(self):
        self.assertEqual(lib_error.AnyDoAPIBinderError('test').__str__(),
                         'test')
