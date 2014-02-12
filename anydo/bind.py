# -*- coding: utf-8 -*-
def bind_method(**config):
    class AnyDoAPIMethod(object):
        path = config['path']
        method = config['method']

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.parameters = {}
            self.id = kwargs.get('id') if kwargs.get('id') else ''

        def execute(self):
            if self.method == 'GET':
                return self.api.get('%s%s/%s' % (self.api.host, self.path, self.id))


    def _call(api, *args, **kwargs):
        method = AnyDoAPIMethod(api, *args, **kwargs)
        return method.execute()

    return _call
