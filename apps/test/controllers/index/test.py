# -*- coding: utf-8 -*-
import json
import unittest2

from manage import app


class Test(unittest2.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data)
        self.assertEqual(data['data'], 'Index')

if __name__ == '__main__':
    unittest2.main()
