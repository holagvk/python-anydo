# -*- coding: utf-8 -*-
""" anydo.lib.tests.test_error """

import unittest
from anydo import error
from anydo.lib import error as lib_error


class ErrorTests(unittest.TestCase):
    """ unit test of anydo.error and anydo.lib.error """

    def test_error_msg(self):
        """ unit test error_msg of anydo.error """
        self.assertEqual(error.AnyDoAPIError('dummy', 'test').__str__(),
                         '(dummy): test')

    def test_lib_error_msg(self):
        """ unit test error_msg of anydo.lib.error """
        self.assertEqual(lib_error.AnyDoAPIBinderError('test').__str__(),
                         'test')
