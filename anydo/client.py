import auth
from bind import bind_method


class AnyDoAPI(auth.AnyDoSession):
    host = "https://sm-prod.any.do"

    def __init__(self, username, password):
        super(AnyDoAPI, self).__init__(username=username,
                                       password=password)

    user_info = bind_method(path="/me",
                            method="GET")
