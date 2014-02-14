# -*- coding: utf-8 -*-
import unittest
from mock import patch
import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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

    @patch('requests.adapters.HTTPAdapter.send')
    def test_user_info(self, m):
        r = self.api.user_info()
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_tasks(self, m):
        r = self.api.tasks(responseType="flat",
                           includeDeleted="false",
                           includeDone="false")
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_categories(self, m):
        r = self.api.categories(responseType="flat",
                                includeDeleted="false",
                                includeDone="false")
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    def test_task(self):
        tasks = self.api.tasks(responseType="flat",
                               includeDeleted="false",
                               includeDone="false")
        if tasks.status_code == 200 and tasks.json():
            task_id = tasks.json()[0].get("id")
            r = self.api.task(uuid=task_id)
            self.assertEqual(r.status_code, 200)

    def test_delete_task(self):
        tasks = self.api.tasks(responseType="flat",
                               includeDeleted="false",
                               includeDone="false")
        if tasks.status_code == 200 and tasks.json():
            task_id = tasks.json()[0].get("id")
            r = self.api.delete_task(uuid=task_id)
            self.assertEqual(r.status_code, 204)

    def test_delete_category(self):
        categories = self.api.categories(responseType="flat",
                                         includeDeleted="false",
                                         includeDone="false")
        if categories.status_code == 200 and categories.json():
            category_id = categories.json()[0].get("id")
            r = self.api.delete_category(uuid=category_id)
            self.assertEqual(r.status_code, 204)

if __name__ == '__main__':
    unittest.main()
