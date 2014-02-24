# -*- coding: utf-8 -*-
import unittest
from mock import patch
import sys
import time
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib import settings
from anydo.lib import utils


class TestAnyDoAPIBinder(AnyDoAPIBinder):
    def __getattribute__(self, attr):
        val = super(TestAnyDoAPIBinder, self).__getattribute__(attr)
        return val


class AnyDoAPIBinderTests(unittest.TestCase):
    setup_done = False  # #TODO: setUpClass ?

    def setUp(self):
        if not self.setup_done:
            super(AnyDoAPIBinderTests, self).setUp()
            self.__class__.api = TestAnyDoAPIBinder(username=settings.USERNAME,
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

    @patch('requests.adapters.HTTPAdapter.send')
    def test_task(self, m):
        task_id = utils.create_uuid()
        r = self.api.task(uuid=task_id)
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_delete_task(self, m):
        task_id = utils.create_uuid()
        r = self.api.delete_task(uuid=task_id)
        r.status_code = 204
        m.return_value = r
        self.assertEqual(r.status_code, 204)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_delete_category(self, m):
        category_id = utils.create_uuid()
        r = self.api.delete_category(uuid=category_id)
        r.status_code = 204
        m.return_value = r
        self.assertEqual(r.status_code, 204)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_category(self, m):
        id = utils.create_uuid()
        r = self.api.create_category(name="ANY.DO_TEST_CATEGORY",
                                     default="false",
                                     isDefault="false",
                                     listPosition="null",
                                     id=id)
        r.status_code = 201
        m.return_value = r
        self.assertEqual(r.status_code, 201)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_task(self, m):
        category_id = utils.create_uuid()
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
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_note(self, m):
        task_id = utils.create_uuid()
        category_id = utils.create_uuid()
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
        r.status_code = 200
        m.return_value = r
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
