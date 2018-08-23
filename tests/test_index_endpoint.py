from tests.setup_tests import BaseTest


class EndpointTestCase(BaseTest):
    ''' API routes test suite '''

    def test_index_endpoint(self):
        ''' Base route should work '''
        req = self.client.get('/api/v1/')

        self.assertEqual(req.status_code, 200)
