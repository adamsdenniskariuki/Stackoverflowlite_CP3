from tests.setup_tests import BaseTest


class RoutesTestCase(BaseTest):
    ''' API routes test suite '''

    def test_base_route(self):
        ''' Base route should work '''
        req = self.client.get('/api/v1/')

        self.assertEqual(req.status_code, 200)
