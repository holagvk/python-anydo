# -*- coding: utf-8 -*-
import unittest
from mock import patch
import sys
import time
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anydo.api import AnyDoAPI
from anydo.lib import settings
from anydo.lib import utils


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
    def test_get_user_info(self, m):
        r = self.api.get_user_info()
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_get_all_tasks(self, m):
        r = self.api.get_all_tasks(include_delete="false",
                                   include_done="false")
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_get_all_categories(self, m):
        r = self.api.get_all_categories(include_delete="false",
                                        include_done="false")
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_get_all_task(self, m):
        tasks = self.api.get_all_tasks(include_delete="false",
                                       include_done="false")
        if tasks.status_code == 200 and tasks.json():
            task_id = tasks.json()[0].get("id")
            r = self.api.task(uuid=task_id)
            self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_delete_task(self, m):
        tasks = self.api.get_all_tasks(include_delete="false",
                                       include_done="false")
        if tasks.status_code == 200 and tasks.json():
            task_id = tasks.json()[0].get("id")
            r = self.api.delete_task(uuid=task_id)
            self.assertEqual(r.status_code, 204)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_delete_category(self, m):
        categories = self.api.get_all_categories(include_delete="false",
                                                 include_done="false")
        if categories.status_code == 200 and categories.json():
            category_id = categories.json()[0].get("id")
            r = self.api.delete_category(uuid=category_id)
            self.assertEqual(r.status_code, 204)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_category(self, m):
        id = utils.create_uuid()
        r = self.api.create_category("ANY.DO_TEST_CATEGORY",
                                     id,
                                     default="false",
                                     is_default="false",
                                     list_position="null")
        r.status_code = 201
        m.return_value = r
        self.assertEqual(r.status_code, 201)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_task(self, m):
        categories = self.api.get_all_categories(include_delete="false",
                                                 include_done="false")
        if categories.status_code == 200 and categories.json():
            category_id = categories.json()[0].get("id")
            task_id = utils.create_uuid()
            r = self.api.create_task(title="ANY.DO_TEST_TASK",
                                     listPositionByCategory=0,
                                     listPositionByPriority=0,
                                     listPositionByDueDate=0,
                                     status="UNCHECKED",
                                     repeatingMethod="TASK_REPEAT_OFF",
                                     shared="false",
                                     priority="Normal",
                                     creationDate=str(int(time.time())),
                                     taskExpanded="false",
                                     categoryID=str(category_id),
                                     dueDate=None,
                                     id=task_id)
            self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_note(self, m):
        # Fetch available categories
        categories = self.api.get_all_categories(include_delete="false",
                                                 include_done="false")
        if categories.status_code == 200 and categories.json():
            category_id = categories.json()[0].get("id")
            task_id = utils.create_uuid()
            # Create task
            new_task = self.api.create_task(title="ANY.DO.TEST_TASK_NOTE",
                                            listPositionByCategory=0,
                                            listPositionByPriority=0,
                                            listPositionByDueDate=0,
                                            status="UNCHECKED",
                                            repeatingMethod="TASK_REPEAT_OFF",
                                            shared="false",
                                            priority="Normal",
                                            creationDate=str(int(time.time())),
                                            taskExpanded="false",
                                            categoryID=str(category_id),
                                            dueDate=None,
                                            id=task_id)
            if new_task.status_code == 200 and new_task.json():
                note_id = utils.create_uuid()
                # Add note in task
                r = self.api.create_task(title="ANY.DO_TEST_NOTE",
                                         listPositionByCategory=0,
                                         listPositionByPriority=0,
                                         listPositionByDueDate=0,
                                         status="UNCHECKED",
                                         repeatingMethod="TASK_REPEAT_OFF",
                                         shared="false",
                                         priority="Normal",
                                         creationDate=str(int(time.time())),
                                         taskExpanded="false",
                                         parentGlobalTaskId=task_id,
                                         categoryID=str(category_id),
                                         dueDate=None,
                                         id=note_id)
                self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
