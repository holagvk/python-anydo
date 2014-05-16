# -*- coding: utf-8 -*-
""" anydo.lib.bind """
from anydo.lib.utils import encode_string
from anydo.lib.error import AnyDoAPIBinderError
from anydo.lib.auth import AnyDoSession
import re
import json
PATH_TEMPLATE = re.compile(r"{\w+}")  # #To support {variable} in paths


def bind_method(**config):
    """
    Binds Any.Do REST API to AnyDoAPIBinder()
    """
    class AnyDoAPIBinderMethod(object):
        """ Method class for AnyDoAPIBinder """
        path = config['path']
        method = config['method']
        accepts_parameters = config.get("accepts_parameters", [])

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.parameters = {}
            self._build_parameters(*args, **kwargs)
            self._build_path()

        def _build_parameters(self, *args, **kwargs):
            """ building parameters sending to API.
            :param *args:
            :param **kwargs:
            """
            for index, value in enumerate(args):
                if value is None:
                    continue

                try:
                    self.parameters[self.accepts_parameters[index]] = \
                        encode_string(value)
                except IndexError:
                    raise AnyDoAPIBinderError("Index Overflow")

            for key, value in kwargs.items():
                if value is None:
                    continue

                if key in self.parameters:
                    raise AnyDoAPIBinderError(
                        "Already have %s as %s" % (key, self.parameters[key])
                    )

                self.parameters[key] = encode_string(value)

        def _build_path(self):
            """ building API path. """
            for var in PATH_TEMPLATE.findall(self.path):
                name = var.strip("{}")

                try:
                    value = self.parameters[name]
                except KeyError:
                    raise AnyDoAPIBinderError("Could not find %s" % name)
                del self.parameters[name]  # #Python won my heart!

                self.path = self.path.replace(var, value)

        def execute(self):
            """ executing API calling. """
            if self.method == 'GET':
                return self.api.get(self.api.host + self.path,
                                    params=self.parameters)
            if self.method == 'DELETE':
                return self.api.delete(self.api.host + self.path)
            if self.method == 'POST':
                data = []
                data.append(self.parameters)
                return self.api.post(self.api.host + self.path,
                                     data=str(json.dumps([item
                                                          for item in data])),
                                     headers={'Content-Type':
                                              'application/json'})
            if self.method == 'PUT':
                return self.api.put(self.api.host + self.path,
                                    data=str(json.dumps(self.parameters)),
                                    headers={'Content-Type':
                                             'application/json'})

    def _call(self, *args, **kwargs):
        """
        :param *args:
        :param **kwargs:
        """
        # self=AnyDoAPIBinder(); satisfy pychecker
        method = AnyDoAPIBinderMethod(self, *args, **kwargs)
        return method.execute()

    return _call


class AnyDoAPIBinder(AnyDoSession):
    """ Binder of AnyDoSession class """
    host = "https://sm-prod.any.do"

    def __init__(self, username, password):
        super(AnyDoAPIBinder, self).__init__(username=username,
                                             password=password)

    # Fetches user information
    user_info = bind_method(path="/me",
                            method="GET")

    # Fetches tasks (including notes)
    tasks = bind_method(path="/me/tasks",
                        method="GET",
                        accepts_parameters=["responseType",
                                            "includeDeleted",
                                            "includeDone"])

    # Fetches categories
    categories = bind_method(path="/me/categories",
                             method="GET",
                             accepts_parameters=["responseType",
                                                 "includeDeleted",
                                                 "includeDone"])

    # Fetches task/note by UUID
    task = bind_method(path="/me/tasks/{uuid}",
                       method="GET",
                       accepts_parameters=["uuid"])

    # Deletes a task/note by UUID
    delete_task = bind_method(path="/me/tasks/{uuid}",
                              method="DELETE",
                              accepts_parameters=["uuid"])

    # Deletes a category by UUID
    delete_category = bind_method(path="/me/categories/{uuid}",
                                  method="DELETE",
                                  accepts_parameters=["uuid"])

    # Creates a new category
    create_category = bind_method(path="/me/categories",
                                  method="POST",
                                  accepts_parameters=["name",
                                                      "default",
                                                      "isDefault",
                                                      "listPosition",
                                                      "id"])

    # Creates a new task/note
    create_task = bind_method(path="/me/tasks",
                              method="POST",
                              accepts_parameters=["title",
                                                  "listPositionByCategory",
                                                  "listPositionByPriority",
                                                  "listPositionByDueDate",
                                                  "status",
                                                  "repeatingMethod",
                                                  "shared",
                                                  "priority",
                                                  "creationDate",
                                                  "taskExpanded",
                                                  "parentGlobalTaskId",
                                                  "categoryId",
                                                  "dueDate",
                                                  "id"])
