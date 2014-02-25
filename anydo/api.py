# -*- coding: utf-8 -*-
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib.utils import create_uuid
from anydo.error import AnyDoAPIError
import time


class AnyDoAPI(object):
    def __init__(self, username=None, password=None, auth_token=None):
        self.api = AnyDoAPIBinder(username, password)
        self.owner_id = self.get_user_info().get('id')
        self.def_category_id = [value for key, value in
                                enumerate(self.get_all_categories())
                                if value['isDefault'] is True][0].get('id')

    def get_user_info(self):
        r = self.api.user_info()
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_all_tasks(self, response_type="flat",
                      include_deleted=False,
                      include_done=False):
        r = self.api.tasks(response_type,
                           include_deleted,
                           include_done)
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_all_categories(self, response_type="flat",
                           include_deleted=False,
                           include_done=False):
        r = self.api.categories(response_type,
                                include_deleted,
                                include_done)
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_task_by_id(self, task_id):
        r = self.api.task(uuid=task_id)
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def delete_task_by_id(self, task_id):
        r = self.api.delete_task(uuid=task_id)
        if r.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % r.status_code)

    def delete_category_by_id(self, category_id):
        if category_id == self.def_category_id:
            raise AnyDoAPIError(422, "Invalid Operation")
        r = self.api.delete_category(uuid=category_id)
        if r.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % r.status_code)

    def create_new_category(self, category_name,
                            default=False,
                            listPosition='null'):
        r = self.api.create_category(category_name,
                                     default,
                                     isDefault="true" if default else "false",
                                     listPosition=listPosition,
                                     id=create_uuid())
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def create_someday_task(self, task_title):
        r = self.api.create_task(task_title,
                                 listPositionByCategory=0,
                                 listPositionByPriority=0,
                                 listPositionByDueDate=0,
                                 status="UNCHECKED",
                                 repeatingMethod="TASK_REPEAT_OFF",
                                 shared="false",
                                 priority="Normal",
                                 creationDate=int(time.time()),
                                 taskExpanded=False,
                                 categoryId=self.def_category_id,
                                 dueDate=None,
                                 id=create_uuid())
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def create_today_task(self, task_title):
        r = self.api.create_task(task_title,
                                 listPositionByCategory=0,
                                 listPositionByPriority=0,
                                 listPositionByDueDate=0,
                                 status="UNCHECKED",
                                 repeatingMethod="TASK_REPEAT_OFF",
                                 shared="false",
                                 priority="Normal",
                                 creationDate=int(time.time()),
                                 taskExpanded=False,
                                 categoryId=self.def_category_id,
                                 dueDate=0,
                                 id=create_uuid())
        try:
            return r.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")
