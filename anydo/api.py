# -*- coding: utf-8 -*-
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib.utils import create_uuid
from anydo.error import AnyDoAPIError
import time


class AnyDoAPI(object):
    def __init__(self, username=None, password=None):
        self.api = AnyDoAPIBinder(username, password)
        self.owner_id = self.get_user_info().get('id')
        self.def_category_id = [value for key, value in
                                enumerate(self.get_all_categories())
                                if value['isDefault'] is True][0].get('id')

    def get_user_info(self):
        """ Fetches user information

            Retrieves information of currently authenticated user

            Args:
                None

            Returns:
                A dictionary of following user information:
                    {'anonymous': Boolean,
                    'creationDate': Number,
                    'email': String,
                    'emails': Array,
                    'facebookAccessToken': String,
                    'facebookId': String,
                    'fake': Boolean,
                    'id': String,
                    'name': String,
                    'phoneNumbers': Array}

            Raises:
                AnyDoAPIError:
                    Code(420): JSON Decoding Error.
        """
        ret = self.api.user_info()
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_all_tasks(self, response_type="flat",
                      include_deleted=False,
                      include_done=False):
        ret = self.api.tasks(response_type,
                             include_deleted,
                             include_done)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_all_categories(self, response_type="flat",
                           include_deleted=False,
                           include_done=False):
        ret = self.api.categories(response_type,
                                  include_deleted,
                                  include_done)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_task_by_id(self, task_id):
        ret = self.api.task(uuid=task_id)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def delete_task_by_id(self, task_id):
        ret = self.api.delete_task(uuid=task_id)
        if ret.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % ret.status_code)

    def delete_category_by_id(self, category_id):
        if category_id == self.def_category_id:
            raise AnyDoAPIError(422, "Invalid Operation")
        ret = self.api.delete_category(uuid=category_id)
        if ret.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % ret.status_code)

    def create_new_category(self, category_name,
                            default=False,
                            list_position='null'):
        ret = self.api.create_category(category_name,
                                       default,
                                       isDefault="true" if default
                                       else "false",
                                       listPosition=list_position,
                                       id=create_uuid())
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def create_new_task(self, task_title, due_day='someday'):
        try:
            ret = self.api.create_task(task_title,
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
                                       dueDate={'someday': None,
                                                'today': 0}[due_day],
                                       id=create_uuid())
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")
        except KeyError:
            raise AnyDoAPIError(422, "Invalid Operation")
