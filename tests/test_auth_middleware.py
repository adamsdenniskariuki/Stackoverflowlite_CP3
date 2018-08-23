from flask import json
from tests.setup_tests import BaseTest


class AuthTestCase(BaseTest):
    ''' Auth middleware test suite '''

    def test_access_endpoint_success(self):
        ''' Should give access to endpoint when token is valid '''
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )

        self.assertEqual(req.status_code, 200)

    def test_no_token(self):
        ''' Should not give access to endpoint when token is not given '''
        req = self.client.post('/api/v1/questions',
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )

        self.assertEqual(req.status_code, 401)

    def test_bad_token(self):
        ''' Should not give access to endpoint when token is not valid '''
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization="bad_token"),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )

        self.assertEqual(req.status_code, 401)
