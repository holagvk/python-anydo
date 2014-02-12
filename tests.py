# -*- coding: utf-8 -*-
import unittest

from anydo.client import AnyDoAPI
from anydo import settings


class TestAnyDoAPI(AnyDoAPI):
    def __getattribute__(self, attr):
        val = super(TestAnyDoAPI, self).__getattribute__(attr)
        return val


class AnyDoAPITests(unittest.TestCase):
    def setUp(self):
        super(AnyDoAPITests, self).setUp()
        self.api = TestAnyDoAPI(username=settings.USERNAME,
                                password=settings.PASSWORD)

    def test_user_info(self):
        r = self.api.user_info()
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
