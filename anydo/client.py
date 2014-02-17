# -*- coding: utf-8 -*-
import auth
from bind import bind_method


class AnyDoAPI(auth.AnyDoSession):
    host = "https://sm-prod.any.do"

    def __init__(self, username, password):
        super(AnyDoAPI, self).__init__(username=username,
                                       password=password)

    """
    Fetches user information
    """
    user_info = bind_method(path="/me",
                            method="GET")

    """
    Fetches tasks (including notes)
    """
    tasks = bind_method(path="/me/tasks",
                        method="GET",
                        accepts_parameters=["responseType",
                                            "includeDeleted",
                                            "includeDone"
                                            ]
                        )

    """
    Fetches categories
    """
    categories = bind_method(path="/me/categories",
                             method="GET",
                             accepts_parameters=["responseType",
                                                 "includeDeleted",
                                                 "includeDone"
                                                 ]
                             )

    """
    Fetches task/note by UUID
    """
    task = bind_method(path="/me/tasks/{uuid}",
                       method="GET",
                       accepts_parameters=["uuid"]
                       )

    """
    Deletes a task/note by UUID
    """
    delete_task = bind_method(path="/me/tasks/{uuid}",
                              method="DELETE",
                              accepts_parameters=["uuid"])

    """
    Deletes a category by UUID
    """
    delete_category = bind_method(path="/me/categories/{uuid}",
                                  method="DELETE",
                                  accepts_parameters=["uuid"])

    """
    Creates a new category
    """
    create_category = bind_method(path="/me/categories",
                                  method="POST",
                                  accepts_parameters=["name",
                                                      "default",
                                                      "isDefault",
                                                      "listPosition",
                                                      "id"])
