from flask import json
from tests.setup_tests import BaseTest


class UserTestCase(BaseTest):
    ''' User test suite '''
    
    def test_signup(self):
        ''' Should register a new user '''
        user_info = dict(email='sonia@gmail.com',
                         username='Sonia',
                         password='Very_secret')
        result = self.client.post('/api/v1/signup',
                                  data=json.dumps(user_info),
                                  content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_email_exists(self):
        ''' Should not register user with an already existing email '''
        result = self.client.post('/api/v1/signup',
                                  data=json.dumps(self.user_data),
                                  content_type='application/json')
        self.assertEqual(result.status_code, 409)

    def test_empty_email_signup(self):
        ''' Should not register user with a missing email '''
        result = self.client.post('/api/v1/signup',
                                  data=json.dumps(dict(
                                    username='Pdiddy',
                                      email=" ",
                                      password='som-wrong'
                                  )),
                                  content_type='application/json')
        self.assertEqual(result.status_code, 400)
    
    def test_empty_pass_signup(self):
        ''' Should not register user with a missing password '''
        result = self.client.post('/api/v1/signup',
                                  data=json.dumps({
                                      "username":"Pdiddy",
                                      "email": 'sample@domain.com',
                                      "password": " "
                                  }),
                                  content_type='application/json')

        self.assertEqual(result.status_code, 400)

    def test_user_login(self):
        ''' Should log in an existing user '''
        user_info = dict(email='domain@gmail.com',
                         username='JohnDoe',
                         password='Very_secret')
        self.client.post('/api/v1/signup',
                                  data=json.dumps(user_info),
                                  content_type='application/json')
        result = self.client.post('/api/v1/login',
                                  data=json.dumps(user_info),
                                  content_type='application/json')
        self.assertEqual(result.status_code, 200)
    
    #def test_email_format_login(self):

    def test_incorrect_email_login(self):
        ''' Should not login user using wrong email '''
        result = self.client.post('/api/v1/login',
                                  data=json.dumps(dict(
                                      email='wrong@domain.com',
                                      password='Very_secret'
                                  )),
                                  content_type='application/json')
        self.assertEqual(result.status_code, 401)

    def test_incorrect_password_login(self):
        ''' Should not login user using wrong password '''
        result = self.client.post('/api/v1/login',
                                  data=json.dumps(dict(
                                      email='sample@domain.com',
                                      password='som-wrong'
                                  )),
                                  content_type='application/json')

        self.assertEqual(result.status_code, 401)

    def test_empty_email_login(self):
        ''' Should not login user with a missing parameter '''
        result = self.client.post('/api/v1/login',
                                  data=json.dumps({
                                      "email": '',
                                      "password": "password"
                                  }),
                                  content_type='application/json')

        self.assertEqual(result.status_code, 400)

    def test_user_logout(self):
        ''' Should log out user '''
        token = self.auth()

        # logout user
        logout = self.client.post('/api/v1/logout',
                                 headers=dict(Authorization=token))
        self.assertEqual(logout.status_code, 200)

        # test if token was blacklisted
        req2 = self.client.get('/api/v1/questions',
                              headers=dict(Authorization=token))

        self.assertEqual(req2.status_code, 401)
