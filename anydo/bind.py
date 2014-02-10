def bind_method(**config):
    class AnyDoAPIMethod(object):
        path = config['path']
        method = config['method']

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.parameters = {}

        def execute(self):
            pass

    def _call(api, *args, **kwargs):
        method = AnyDoAPIMethod(api, *args, **kwargs)
        return method.execute()

    return _call
