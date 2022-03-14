import unittest


def setUpModule():
    print('setting up module...')


def tearDownModule():
    print('tearing down module...')


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'setting up class... {cls.__name__}')

    @classmethod
    def tearDownClass(cls):
        print(f'tearing down class... {cls.__name__}')

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')


class TestClass2(unittest.TestCase):

    def setUp(self):
        print('setting up...')

    def tearDown(self):
        print('tearing down...')

    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')
