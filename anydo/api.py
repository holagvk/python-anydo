# -*- coding: utf-8 -*-
""" anydo.api """
from anydo.lib.bind import AnyDoAPIBinder
from anydo.lib.utils import create_uuid
from anydo.error import AnyDoAPIError
import time


class AnyDoAPI(object):
    """ Base class that all AnyDo API client"""
    def __init__(self, username=None, password=None):
        self.api = AnyDoAPIBinder(username, password)

    def owner_id(self):
        """ Retrieve owner id.
        Returns: owner id of AnyDo task
        """
        return self.get_user_info().get('id')

    def default_category_id(self):
        """ Retrieve default category id.
        Returns: default category id of AnyDo tasks
        """
        return [value for _, value in
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
        """ retrieve all tasks.
        Returns: List of all tasks
        :param response_type: "flat" in default
        :param include_deleted: False in default
        :param include_done: False in default
        """
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
        """ retrieve all categories.
        Returns: List of all categories
        :param response_type: "flat" in default
        :param include_deleted: False in default
        :param include_done: False in default
        """
        ret = self.api.categories(response_type,
                                  include_deleted,
                                  include_done)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_task_by_id(self, task_id):
        """ retrieve task specified task id.
        Returns: Dictionary of task
        :param task_id: task id formatted uuid
        """
        ret = self.api.task(uuid=task_id)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def delete_task_by_id(self, task_id):
        """ delete task specified task id.
        :param task_id: task id formatted uuid
        """
        ret = self.api.delete_task(uuid=task_id)
        if ret.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % ret.status_code)

    def delete_category_by_id(self, category_id):
        """ delete category specified category id.
        :param category_id: category id formatted uuid
        """
        if category_id == self.default_category_id():
            raise AnyDoAPIError(422, "Invalid Operation")
        ret = self.api.delete_category(uuid=category_id)
        if ret.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % ret.status_code)

    def create_new_category(self, category_name,
                            default=False,
                            list_position='null'):
        """ create a new category.
        Returns: Dictionary of category
        :param category_name: string of category name
        :param default: False in default
        :param list_position: 'null' in default
        """
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
        """ create a new task.
        Returns: Dictionary of task
        :param task_title: string of task title
        :param due_day: 'someday' in default
        """
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
                                       categoryId=self.default_category_id(),
                                       dueDate={'someday': None,
                                                'today': 0}[due_day],
                                       id=create_uuid())
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")
        except KeyError:
            raise AnyDoAPIError(422, "Invalid Operation")
