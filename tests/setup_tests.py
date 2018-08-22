from flask import json
import unittest
import config
from db import create_tables
from stackoverflowlite import app
from stackoverflowlite.models.users import User
from db.dbconfig import open_test_connection,close_connection


class BaseTest(unittest.TestCase):
    ''' Base test configurations '''
    def setUp(self):
        ''' Configuration settings before testing starts '''
        create_tables.create_test_tables()
        self.client = app.test_client()
        self.client.testing = True
        self.user_data = {
            "email": 'example@domain.com',
            "username": 'Name',
            "password": 'secret'
        }
        self.question = {"description": "How do I use unittest?"}
        self.answer = {
            "answer": "This is how you do it"}

    def auth(self):
        ''' Provide authorization token during testing '''
        result = self.client.post('/api/v1/login',
                                  data=json.dumps(dict(
                                      email='example@domain.com',
                                      password='secret'
                                  )), 
                                  content_type='application/json')

        user_jwt = json.loads(result.data.decode("utf-8"))['token']
        return user_jwt
        
    def tearDown(self):
        create_tables.drop_test_db()




