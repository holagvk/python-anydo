import auth

class AnyDoAPI(auth.AuthBase):
    auth_url = "https://sm-prod.any.do/j_spring_security_check"
    def __init__(self, username, password, sec_rem="on"):
	self.auth_args = dict()
	self.auth_args['j_username'] = username
	self.auth_args['j_password'] = password
	self.auth_args['_spring_security_remember_me'] = sec_rem
        super(AnyDoAPI, self).__init__(AnyDoAPI.auth_url, self.auth_args)
