# -*- coding: utf-8 -*-
import requests
from anydo import settings


class AnyDoSession(object):
    """Authenticates with Any.Do"""
    def __init__(self, username=None, password=None):
        self.session = requests.session()
        AnyDoSession.post(self,
                          url='https://sm-prod.any.do/j_spring_security_check',
                          data={'j_username': username, 'j_password': password,
                                '_spring_security_remember_me': 'on'},
                          headers={'content-type':
                                   'application/x-www-form-urlencoded'}
                          )

    def get(self, url, **kwargs):
        return self.session.get(url, proxies=settings.PROXIES, **kwargs)

    def post(self, url, data=None, **kwargs):
        return self.session.post(url, data, proxies=settings.PROXIES, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(url, proxies=settings.PROXIES, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.session.put(url, data, proxies=settings.PROXIES, **kwargs)
