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

    def __owner_id(self):
        """ Retrieve owner id.
        Returns: owner id of AnyDo task
        """
        return self.get_user_info().get('id')

    def __default_category_id(self):
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
        """ Retrieve all tasks

            Args:
                response_type: "flat" in default
                include_deleted: False in default
                include_done: False in default

            Returns:
                A list of all tasks

            Raises:
                AnyDoAPIError:
                    Code(420): JSON Decoding Error.
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
        """ Retrieve all categories

            Args:
                response_type: "flat" in default
                include_deleted: False in default
                include_done: False in default

            Returns:
                A list of all categories

            Raises:
                AnyDoAPIError:
                    Code(420): JSON Decoding Error.
        """
        ret = self.api.categories(response_type,
                                  include_deleted,
                                  include_done)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def get_task_by_id(self, task_id):
        """ Retrieve a task specified by id

            Args:
                task_id: task id formatted uuid

            Returns:
                A dictionary of task

            Raises:
                AnyDoAPIError:
                    Code(420): JSON Decoding Error.
        """
        ret = self.api.task(uuid=task_id)
        try:
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")

    def delete_task_by_id(self, task_id):
        """ Delete a task specified by id

            Args:
                task_id: task id formatted uuid

            Returns:
                None

            Raises:
                AnyDoAPIError:
                    Code(421): HTTP Error Code.
        """
        ret = self.api.delete_task(uuid=task_id)
        if ret.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % ret.status_code)

    def delete_category_by_id(self, category_id):
        """ Delete a category specified by id

            Args:
                category_id: category id formatted uuid

            Returns:
                None

            Raises:
                AnyDoAPIError:
                    Code(421): HTTP Error Code.
                    Code(422): Invalid Operation.
        """
        if category_id == self.__default_category_id():
            raise AnyDoAPIError(422, "Invalid Operation")
        ret = self.api.delete_category(uuid=category_id)
        if ret.status_code != 204:
            raise AnyDoAPIError(421, "HTTP Error %d" % ret.status_code)

    def create_new_category(self, category_name,
                            default=False,
                            list_position='null'):
        """ Create a new category

            Args:
                category_name: string of category name
                default: False in default
                list_position: 'null' in default

            Returns:
                A dictionary of category

            Raises:
                AnyDoAPIError:
                    Code(420): JSON Decoding Error.
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
        """ Create a new task

            Args:
                task_title: string of task title
                due_day: 'someday' in default

            Returns:
                A dictionary of task

            Raises:
                AnyDoAPIError:
                    Code(420): JSON Decoding Error.
                    Code(422): Invalid Operation
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
                                       categoryId=self.__default_category_id(),
                                       dueDate={'someday': None,
                                                'today': 0}[due_day],
                                       id=create_uuid())
            return ret.json()
        except ValueError:
            raise AnyDoAPIError(420, "JSON Decoding Error")
        except KeyError:
            raise AnyDoAPIError(422, "Invalid Operation")
