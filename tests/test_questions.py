from flask import json
from tests.setup_tests import BaseTest


class questionTestCase(BaseTest):
    ''' question test suite '''

    def test_post_question(self):
        ''' Should create a new question '''
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )

        self.assertEqual(req.status_code, 200)
    
    def test_question_exists(self):
        ''' Should not create question if question exists '''
        token = self.auth()
        req1 = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )
        
        req2 = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )

        self.assertEqual(req2.status_code, 409)

    def test_empty_question(self):
        ''' Should not create question without description '''
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps({"description": " "})
                               )

        self.assertEqual(req.status_code, 400)

    def test_question_format(self):
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/not_json',
                               data=json.dumps(self.question)
                               )
        self.assertEqual(req.status_code, 400)

    def test_get_question(self):
        ''' Should view an existing question '''
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )
        req = self.client.get('/api/v1/questions/1',
                                 headers=dict(Authorization=token),
                                 content_type='application/json'
                                 )
        self.assertEqual(req.status_code, 200)

    def test_delete_question(self):
        ''' Should delete an existing question '''
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )
        deleted = self.client.delete('/api/v1/questions/1',
                                 headers=dict(Authorization=token))

        self.assertEqual(deleted.status_code, 200)

    def test_wrong_question_id(self):
        ''' Should return error when non-existent question id is given '''
        token = self.auth()
        req = self.client.delete('/api/v1/questions/1000',
                                     headers=dict(Authorization=token))
        self.assertEqual(req.status_code, 404)

    def test_post_answer(self):
        token = self.auth()
        self.client.post('/api/v1/questions',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.question)
                               )
        response = self.client.post('/api/v1/questions/1/answers',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.answer)
                               )
        self.assertEqual(response.status_code, 200)

    def test_post_answer_question_not_found(self):
        token = self.auth()
        response = self.client.post('/api/v1/questions/1/answers',
                                    headers=dict(Authorization=token),
                                    content_type='application/json',
                                    data=json.dumps(self.answer)
                                    )
        self.assertEqual(response.status_code, 404)

    def test_post_empty_answer(self):
        token = self.auth()
        self.client.post('/api/v1/questions',
                         headers=dict(Authorization=token),
                         content_type='application/json',
                         data=json.dumps(self.question)
                         )
        req = self.client.post('/api/v1/questions/1/answers',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps({"answer":" "})
                               )
        self.assertEqual(req.status_code, 400)

    def post_answer_format(self):
        token = self.auth()
        req = self.client.post('/api/v1/questions',
                         headers=dict(Authorization=token),
                         content_type='application/not_json',
                         data=json.dumps(self.question)
                         )

        self.assertEqual(req.status_code, 400)

    def test_answer_exists(self):
        token = self.auth()
        self.client.post('/api/v1/questions',
                         headers=dict(Authorization=token),
                         content_type='application/json',
                         data=json.dumps(self.question)
                         )
        req1 = self.client.post('/api/v1/questions/1/answers',
                               headers=dict(Authorization=token),
                               content_type='application/json',
                               data=json.dumps(self.answer)
                               )
        req2 = self.client.post('/api/v1/questions/1/answers',
                                headers=dict(Authorization=token),
                                content_type='application/json',
                                data=json.dumps(self.answer)
                                )
        self.assertEqual(req2.status_code, 409)

    def test_get_user_questions(self):
        token = self.auth()
        self.client.post('/api/v1/questions',
                         headers=dict(Authorization=token),
                         content_type='application/json',
                         data=json.dumps(self.question)
                         )
        req = self.client.get('/api/v1/user_questions',
                              headers=dict(Authorization=token),
                              content_type='application/json'
                              )
        self.assertEqual(req.status_code, 200)

    def test_question_answers(self):
        token = self.auth()
        self.client.post('/api/v1/questions',
                         headers=dict(Authorization=token),
                         content_type='application/json',
                         data=json.dumps(self.question)
                         )
        self.client.post('/api/v1/questions/1/answers',
                                    headers=dict(Authorization=token),
                                    content_type='application/json',
                                    data=json.dumps(self.answer)
                                    )
        req = self.client.get('/api/v1/question_answers/1',
                              headers=dict(Authorization=token),
                              content_type='application/json'
                              )
        self.assertEqual(req.status_code, 200)

