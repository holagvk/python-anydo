# -*- coding: utf-8 -*-
from utils import encode_string
from error import AnyDoClientError


def bind_method(**config):
    class AnyDoAPIMethod(object):
        path = config['path']
        method = config['method']
        accepts_parameters = config.get("accepts_parameters", [])

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.parameters = {}
            self._build_parameters(*args, **kwargs)

        def _build_parameters(self, *args, **kwargs):
            for index, value in enumerate(args):
                if value is None:
                    continue

                try:
                    self.parameters[self.accepts_parameters[index]] = \
                        encode_string(value)
                except IndexError:
                    raise AnyDoClientError("Index Overflow")

            for key, value in kwargs.iteritems():
                if value is None:
                    continue

                if key in self.parameters:
                    raise AnyDoClientError(
                        "Already have %s as %s" % (key, self.parameters[key])
                    )

                self.parameters[key] = encode_string(value)

        def execute(self):
            if self.method == 'GET':
                return self.api.get(self.api.host + self.path,
                                    params=self.parameters)

    def _call(api, *args, **kwargs):
        method = AnyDoAPIMethod(api, *args, **kwargs)
        return method.execute()

    return _call
