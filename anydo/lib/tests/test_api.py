# -*- coding: utf-8 -*-

import unittest
from httpretty import HTTPretty, httprettified
from anydo import api
from anydo.error import AnyDoAPIError
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib import settings
from anydo.lib import utils


class AnyDoAPITests(unittest.TestCase):

    @httprettified
    def setUp(self):
        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/j_spring_security_check' % AnyDoAPIBinder.host)
        self.conn = api.AnyDoAPI(username=settings.USERNAME,
                                 password=settings.PASSWORD)

    @httprettified
    def test_get_user_info(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}')
        self.assertDictEqual({'dummy_key': 'dummy_value'},
                             self.conn.get_user_info())

    @httprettified
    def test_get_user_info_fail(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me' % AnyDoAPIBinder.host)
        with self.assertRaises(AnyDoAPIError):
            self.conn.get_user_info()

    @httprettified
    def test_get_all_tasks(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}')
        self.assertDictEqual({"dummy_key": "dummy_value"},
                             self.conn.get_all_tasks())

    @httprettified
    def test_get_all_tasks_fail(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks' % AnyDoAPIBinder.host)
        with self.assertRaises(AnyDoAPIError):
            self.conn.get_all_tasks()

    @httprettified
    def test_get_all_categories(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}')
        self.assertDictEqual({"dummy_key": "dummy_value"},
                             self.conn.get_all_categories())

    @httprettified
    def test_get_all_categories_fail(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host)
        with self.assertRaises(AnyDoAPIError):
            self.conn.get_all_categories()

    @httprettified
    def test_get_task_by_id(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid),
            body='{"dummy_key": "dummy_value"}')
        self.assertDictEqual({"dummy_key": "dummy_value"},
                             self.conn.get_task_by_id(uuid))

    @httprettified
    def test_get_task_by_id_fail(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid))
        with self.assertRaises(AnyDoAPIError):
            self.conn.get_task_by_id(uuid)

    @httprettified
    def test_delete_task_by_id(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid),
            status=204)
        self.assertEqual(None,
                         self.conn.delete_task_by_id(uuid))

    @httprettified
    def test_delete_task_by_id_fail(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/tasks/%s' % (AnyDoAPIBinder.host, uuid),
            status=503)
        with self.assertRaises(AnyDoAPIError):
            self.conn.delete_task_by_id(uuid)

    @httprettified
    def test_delete_category_by_id(self):
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
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='[{"isDefault": true, "id": "dummy_category0"}]')
        HTTPretty.register_uri(
            HTTPretty.DELETE,
            '%s/me/categories/%s' % (AnyDoAPIBinder.host, uuid),
            status=503)
        with self.assertRaises(AnyDoAPIError):
            self.conn.delete_category_by_id(uuid)

    @httprettified
    def test_create_new_category(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='{"dummy_key": "dummy_value"}',
            status=201)
        self.assertDictEqual({"dummy_key": "dummy_value"},
                             self.conn.create_new_category(uuid))

    @httprettified
    def test_create_new_category_fail(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/categories' % AnyDoAPIBinder.host)
        with self.assertRaises(AnyDoAPIError):
            self.conn.create_new_category(uuid)

    @httprettified
    def test_create_new_task(self):
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
        self.assertDictEqual({"dummy_key": "dummy_value"},
                             self.conn.create_new_task(uuid))

    @httprettified
    def test_create_new_task_fail(self):
        uuid = utils.create_uuid()
        HTTPretty.register_uri(
            HTTPretty.GET,
            '%s/me/categories' % AnyDoAPIBinder.host,
            body='[{"isDefault": true, "id": "dummy_category0"}]')

        HTTPretty.register_uri(
            HTTPretty.POST,
            '%s/me/tasks' % AnyDoAPIBinder.host)
        with self.assertRaises(AnyDoAPIError):
            self.conn.create_new_task(uuid)
