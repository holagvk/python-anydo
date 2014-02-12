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

    def test_get_user_info(self):
        r = self.api.get_user_info()
        self.assertEqual(r.status_code, 200)

    def test_get_tasks(self):
        r = self.api.get_tasks()
        self.assertEqual(r.status_code, 200)

    def test_get_task(self):
        r = self.api.get_tasks()
        if r.json():
            task_id = r.json()[0].get('id')
        r2 = self.api.get_task(id=task_id)
        self.assertEqual(r2.status_code, 200)

    def test_get_categories(self):
        r = self.api.get_categories()
        self.assertEqual(r.status_code, 200)

    def test_get_category(self):
        r = self.api.get_categories()
        if r.json():
            category_id = r.json()[0].get('id')
        r2 = self.api.get_category(id=category_id)
        self.assertEqual(r2.status_code, 200)



if __name__ == '__main__':
    unittest.main()
