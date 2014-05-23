# -*- coding: utf-8 -*-
""" anydo.lib.tests.test_lib """
import unittest
from httpretty import HTTPretty, httprettified
import time
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib import settings
from anydo.lib import utils


class TestAnyDoAPIBinder(AnyDoAPIBinder):
    """ unit test of AnyDoAPIBinder class """
    def __getattribute__(self, attr):
        val = super(TestAnyDoAPIBinder, self).__getattribute__(attr)
        return val


class AnyDoAPIBinderTests(unittest.TestCase):
    """ unit test of AnyDoAPIBind """
    setup_done = False  # #TODO: setUpClass ?

    @httprettified
    def setUp(self):
        if not self.setup_done:
            HTTPretty.register_uri(
                HTTPretty.POST,
                '%s/j_spring_security_check' % AnyDoAPIBinder.host)
            super(AnyDoAPIBinderTests, self).setUp()
            self.__class__.api = TestAnyDoAPIBinder(username=settings.USERNAME,
                                                    password=settings.PASSWORD)
            self.__class__.setup_done = True

    @httprettified
    def test_user_info(self):
        """ unit test of user_info """
        HTTPretty.register_uri(HTTPretty.GET,
                               '%s/me' % AnyDoAPIBinder.host)
        ret = self.api.user_info()
        self.assertEqual(ret.status_code, 200)

    @httprettified
    def test_tasks(self):
        """ unit test of tasks """
        HTTPretty.register_uri(HTTPretty.GET,
                               '%s/me/tasks' % AnyDoAPIBinder.host)
        ret = self.api.tasks(responseType="flat",
                             includeDeleted="false",
                             includeDone="false")
        self.assertEqual(ret.status_code, 200)

    @httprettified
    def test_categories(self):
        """ unit test of categories """
        HTTPretty.register_uri(HTTPretty.GET,
                               '%s/me/categories' % AnyDoAPIBinder.host)
        ret = self.api.categories(responseType="flat",
                                  includeDeleted="false",
                                  includeDone="false")
        self.assertEqual(ret.status_code, 200)

    @httprettified
    def test_task(self):
        """ unit test of task """
        task_id = utils.create_uuid()
        HTTPretty.register_uri(HTTPretty.GET,
                               '%s/me/tasks/%s' % (AnyDoAPIBinder.host,
                                                   task_id))
        ret = self.api.task(uuid=task_id)
        self.assertEqual(ret.status_code, 200)

    @httprettified
    def test_delete_task(self):
        """ unit test of delete task """
        task_id = utils.create_uuid()
        HTTPretty.register_uri(HTTPretty.DELETE,
                               '%s/me/tasks/%s' % (AnyDoAPIBinder.host,
                                                   task_id),
                               status=204)
        ret = self.api.delete_task(uuid=task_id)
        self.assertEqual(ret.status_code, 204)

    @httprettified
    def test_delete_category(self):
        """ unit test of delete category """
        category_id = utils.create_uuid()
        HTTPretty.register_uri(HTTPretty.DELETE,
                               '%s/me/categories/%s' % (AnyDoAPIBinder.host,
                                                        category_id),
                               status=204)
        ret = self.api.delete_category(uuid=category_id)
        self.assertEqual(ret.status_code, 204)

    @httprettified
    def test_create_category(self):
        """ unit test of create category """
        category_id = utils.create_uuid()
        HTTPretty.register_uri(HTTPretty.POST,
                               '%s/me/categories' % AnyDoAPIBinder.host,
                               status=201)
        ret = self.api.create_category(name="ANY.DO_TEST_CATEGORY",
                                       default="false",
                                       isDefault="false",
                                       listPosition="null",
                                       id=category_id)
        self.assertEqual(ret.status_code, 201)

    @httprettified
    def test_create_task(self):
        """ unit test of create task """
        category_id = utils.create_uuid()
        task_id = utils.create_uuid()
        HTTPretty.register_uri(HTTPretty.POST,
                               '%s/me/tasks' % AnyDoAPIBinder.host,
                               status=200)
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
        self.assertEqual(ret.status_code, 200)

    @httprettified
    def test_create_note(self):
        """ unit test of create note """
        task_id = utils.create_uuid()
        category_id = utils.create_uuid()
        note_id = utils.create_uuid()
        HTTPretty.register_uri(HTTPretty.POST,
                               '%s/me/tasks' % AnyDoAPIBinder.host)
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
        self.assertEqual(ret.status_code, 200)
