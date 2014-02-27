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
    def test_user_info(self, mock_class):
        ret = self.api.user_info()
        ret.status_code = 200
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_tasks(self, mock_class):
        ret = self.api.tasks(responseType="flat",
                             includeDeleted="false",
                             includeDone="false")
        ret.status_code = 200
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_categories(self, mock_class):
        ret = self.api.categories(responseType="flat",
                                  includeDeleted="false",
                                  includeDone="false")
        ret.status_code = 200
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_task(self, mock_class):
        task_id = utils.create_uuid()
        ret = self.api.task(uuid=task_id)
        ret.status_code = 200
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_delete_task(self, mock_class):
        task_id = utils.create_uuid()
        ret = self.api.delete_task(uuid=task_id)
        ret.status_code = 204
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 204)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_delete_category(self, mock_class):
        category_id = utils.create_uuid()
        ret = self.api.delete_category(uuid=category_id)
        ret.status_code = 204
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 204)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_category(self, mock_class):
        category_id = utils.create_uuid()
        ret = self.api.create_category(name="ANY.DO_TEST_CATEGORY",
                                       default="false",
                                       isDefault="false",
                                       listPosition="null",
                                       id=category_id)
        ret.status_code = 201
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 201)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_task(self, mock_class):
        category_id = utils.create_uuid()
        task_id = utils.create_uuid()
        ret = self.api.create_task(title="ANY.DO_TEST_TASK",
                                   listPositionByCategory=0,
                                   listPositionByPriority=0,
                                   listPositionByDueDate=0,
                                   status="UNCHECKED",
                                   repeatingMethod="TASK_REPEAT_OFF",
                                   shared="false",
                                   priority="Normal",
                                   creationDate=str(int(time.time())),
                                   taskExpanded="false",
                                   categoryId=str(category_id),
                                   dueDate=None,
                                   id=task_id)
        ret.status_code = 200
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 200)

    @patch('requests.adapters.HTTPAdapter.send')
    def test_create_note(self, mock_class):
        task_id = utils.create_uuid()
        category_id = utils.create_uuid()
        note_id = utils.create_uuid()
        # Add note in task
        ret = self.api.create_task(title="ANY.DO_TEST_NOTE",
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
                                   categoryId=str(category_id),
                                   dueDate=None,
                                   id=note_id)
        ret.status_code = 200
        mock_class.return_value = ret
        self.assertEqual(ret.status_code, 200)

if __name__ == '__main__':
    unittest.main()
