import requests

"""
TODO: Handle Exceptions
"""
class AuthBase(object):
    def __init__(self, auth_url=None, auth_args=None):
	self.auth_session = requests.session()
	self.auth_result = AuthBase.requestAuthSessionPost(self, auth_url, auth_args)

    def getAuthSession(self):
	return self.auth_session

    def getAuthResult(self):
	return self.auth_result

    def requestAuthSessionGet(self, url):
	return self.auth_session.get(url)

    def requestAuthSessionPost(self, url, data):
	return self.auth_session.post(url, data)
