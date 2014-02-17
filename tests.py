# -*- coding: utf-8 -*-
import unittest
from anydo.client import AnyDoAPI
from anydo import settings
from anydo import utils


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

    def test_create_category(self):
        id = utils.create_uuid()
        r = self.api.create_category(name="ANY.DO_TEST_CATEGORY",
                                     default="false",
                                     isDefault="false",
                                     listPosition="null",
                                     id=id)
        self.assertEqual(r.status_code, 201)

if __name__ == '__main__':
    unittest.main()
