from flask import json
import unittest
from db import create_tables
from stackoverflowlite import app


class BaseTest(unittest.TestCase):
    ''' Base configurations '''
    def setUp(self):
        ''' setup configurations '''
        create_tables.create_tables()
        self.client = app.test_client()
        self.client.testing = True
        self.user_data = {
            "email": 'mirrmaina@gmail.com',
            "username": 'Mirriam',
            "password": 'password'
        }
        self.question = {"description": "How do I use unittest?"}
        self.answer = {
            "answer": "This is how you do it"}

    def auth(self):
        ''' Add token during testing '''
        user_info = dict(email='emily@gmail.com',
                         username='emily',
                         password='secret')
        self.client.post('/api/v1/signup',
                         data=json.dumps(user_info),
                         content_type='application/json')
        result = self.client.post('/api/v1/login',
                                  data=json.dumps(dict(
                                      email='emily@gmail.com',
                                      password='secret'
                                  )), 
                                  content_type='application/json')

        user_jwt = json.loads(result.data.decode("utf-8"))['token']
        return user_jwt

    def tearDown(self):
        create_tables.drop_tables()




