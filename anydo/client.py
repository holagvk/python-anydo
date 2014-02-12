# -*- coding: utf-8 -*-
import auth
from bind import bind_method


class AnyDoAPI(auth.AnyDoSession):
    host = "https://sm-prod.any.do"

    def __init__(self, username, password):
        super(AnyDoAPI, self).__init__(username=username,
                                       password=password)

    get_user_info = bind_method(path="/me",
                                method="GET")

    get_tasks = bind_method(path="/me/tasks",
                            method="GET")

    get_task = bind_method(path="/me/tasks",
                           method="GET")

    get_categories = bind_method(path="/me/categories",
                                 method="GET")

    # this api returns status code only.
    get_category = bind_method(path="/me/categories",
                               method="GET")
