# -*- coding: utf-8 -*-
import unittest
from anydo.client import AnyDoAPI
from anydo import settings


class TestAnyDoAPI(AnyDoAPI):
    def __getattribute__(self, attr):
        val = super(TestAnyDoAPI, self).__getattribute__(attr)
        return val


class AnyDoAPITests(unittest.TestCase):
    setup_done = False  # #TODO: setUpClass ?

    def setUp(self):
        if not self.setup_done:
            super(AnyDoAPITests, self).setUp()
            self.__class__.api = TestAnyDoAPI(username=settings.USERNAME,
                                              password=settings.PASSWORD)
            self.__class__.setup_done = True

    def test_user_info(self):
        r = self.api.user_info()
        self.assertEqual(r.status_code, 200)

    def test_tasks(self):
        r = self.api.tasks(responseType="flat",
                           includeDeleted="false",
                           includeDone="false")
        self.assertEqual(r.status_code, 200)

    def test_categories(self):
        r = self.api.categories(responseType="flat",
                                includeDeleted="false",
                                includeDone="false")
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
