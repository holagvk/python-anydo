# -*- coding: utf-8 -*-
""" anydo.lib.tests.test_api """

import unittest
from httpretty import HTTPretty, httprettified
from anydo import api
from anydo.error import AnyDoAPIError
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib import settings
from anydo.lib import utils


class AnyDoAPITests(unittest.TestCase):
    """ unit test of anydo.lib.api """

    @httprettified
    def setUp(self):
        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/j_spring_security_check' % AnyDoAPIBinder.host)
        self.conn = api.AnyDoAPI(username=settings.USERNAME,
                                 password=settings.PASSWORD)

    @httprettified
    def test_get_user_info(self):
        """ unit test of get_user_info """
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}')
        self.assertEqual({'dummy_key': 'dummy_value'},
                         self.conn.get_user_info())

    @httprettified
    def test_get_user_info_fail(self):
        """ unit test of get_user_info error case """
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me' % AnyDoAPIBinder.host)
        self.assertRaises(AnyDoAPIError, self.conn.get_user_info)

    @httprettified
    def test_get_all_tasks(self):
        """ unit test of get_all_tasks  """
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}')
        self.assertEqual({"dummy_key": "dummy_value"},
                         self.conn.get_all_tasks())

    @httprettified
    def test_get_all_tasks_fail(self):
        """ unit test of get_all_tasks error case """
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks' % AnyDoAPIBinder.host)
        self.assertRaises(AnyDoAPIError, self.conn.get_all_tasks)

    @httprettified
    def test_get_all_categories(self):
        """ unit test of get_all_categories """
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}')
        self.assertEqual({"dummy_key": "dummy_value"},
                         self.conn.get_all_categories())

    @httprettified
    def test_get_all_categories_fail(self):
        """ unit test of get_all_categories error case """
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host)
        self.assertRaises(AnyDoAPIError, self.conn.get_all_categories)

    @httprettified
    def test_get_task_by_id(self):
        """ unit test of get_task_by_id """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid),
            body='{"dummy_key": "dummy_value"}')
        self.assertEqual({"dummy_key": "dummy_value"},
                         self.conn.get_task_by_id(uuid))

    @httprettified
    def test_get_task_by_id_fail(self):
        """ unit test of get_task_by_id error case """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid))
        self.assertRaises(AnyDoAPIError, self.conn.get_task_by_id, uuid)

    @httprettified
    def test_delete_task_by_id(self):
        """ unit test of delete_task_by_id """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid),
            status=204)
        self.assertEqual(None,
                         self.conn.delete_task_by_id(uuid))

    @httprettified
    def test_delete_task_by_id_fail(self):
        """ unit test of delete_task_by_id error case """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid),
            status=503)
        self.assertRaises(AnyDoAPIError, self.conn.delete_task_by_id, uuid)

    @httprettified
    def test_delete_category_by_id(self):
        """ unit test of delete_category_by_id """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='[{"isDefault": true, "id": "dummy_category0"}]')
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/categories/%s' % (AnyDoAPIBinder.host, uuid),
            status=204)
        self.assertEqual(None,
                         self.conn.delete_category_by_id(uuid))

    @httprettified
    def test_delete_category_by_id_fail(self):
        """ unit test of delete_category_by_id error case """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='[{"isDefault": true, "id": "dummy_category0"}]')
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/categories/%s' % (AnyDoAPIBinder.host, uuid),
            status=503)
        self.assertRaises(AnyDoAPIError, self.conn.delete_category_by_id, uuid)

    @httprettified
    def test_create_new_category(self):
        """ unit test of create_new_category """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}',
            status=201)
        self.assertEqual({"dummy_key": "dummy_value"},
                         self.conn.create_new_category(uuid))

    @httprettified
    def test_create_new_category_fail(self):
        """ unit test of create_new_category error case """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/categories' % AnyDoAPIBinder.host)
        self.assertRaises(AnyDoAPIError, self.conn.create_new_category, uuid)

    @httprettified
    def test_create_new_task(self):
        """ unit test of create_new_task """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='[{"isDefault": true, "id": "dummy_category0"}]')

        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/tasks' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}',
            status=201)
        self.assertEqual({"dummy_key": "dummy_value"},
                         self.conn.create_new_task(uuid))

    @httprettified
    def test_create_new_task_fail(self):
        """ unit test of create_new_task error case """
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='[{"isDefault": true, "id": "dummy_category0"}]')

        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/tasks' % AnyDoAPIBinder.host)
        self.assertRaises(AnyDoAPIError, self.conn.create_new_task, uuid)
