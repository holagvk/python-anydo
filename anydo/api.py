from lib.client import AnyDoClient


class AnyDoAPI():
    def __init__(self, username, password):
        self.client = AnyDoClient(username, password)

    def get_user_info(self):
        return self.client.user_info().json()

    def get_all_tasks(self, include_delete=False, include_done=False):
        return self.client.tasks("flat",
                                 "true" if include_delete else "false",
                                 "true" if include_done else "false").json()

    def get_all_categories(self, include_delete=False, include_done=False):
        return self.client.categories("flat",
                                      "true" if include_delete else "false",
                                      "true" if include_done else "false").json()

    def get_task_by_id(self, task_id):
        return self.client.task(task_id).json()
