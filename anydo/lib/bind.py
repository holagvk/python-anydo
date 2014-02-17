# -*- coding: utf-8 -*-
from anydo.lib.utils import encode_string
from anydo.lib.error import AnyDoClientError
import re
import json
path_template = re.compile("{\w+}")  # #To support {variable} in paths


def bind_method(**config):
    class AnyDoClientMethod(object):
        path = config['path']
        method = config['method']
        accepts_parameters = config.get("accepts_parameters", [])

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.parameters = {}
            self._build_parameters(*args, **kwargs)
            self._build_path()

        def _build_parameters(self, *args, **kwargs):
            for index, value in enumerate(args):
                if value is None:
                    continue

                try:
                    self.parameters[self.accepts_parameters[index]] = \
                        encode_string(value)
                except IndexError:
                    raise AnyDoClientError("Index Overflow")

            for key, value in kwargs.items():
                if value is None:
                    continue

                if key in self.parameters:
                    raise AnyDoClientError(
                        "Already have %s as %s" % (key, self.parameters[key])
                    )

                self.parameters[key] = encode_string(value)

        def _build_path(self):
            for var in path_template.findall(self.path):
                name = var.strip("{}")

                try:
                    value = self.parameters[name]
                except KeyError:
                    raise AnyDoClientError("Could not find %s" % name)
                del self.parameters[name]  # #Python won my heart!

                self.path = self.path.replace(var, value)

        def execute(self):
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
                                              'application/json'}
                                     )

    def _call(self, *args, **kwargs):
        #self=AnyDoClient(); satisfy pychecker
        method = AnyDoClientMethod(self, *args, **kwargs)
        return method.execute()

    return _call
