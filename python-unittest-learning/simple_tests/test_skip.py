import sys
import unittest
from datetime import date


class TestCase(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skip('Always skipping...')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2 != 0, 'Skipping odd days...')
    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2 == 0, 'Skipping even days...')
    def test_case_4(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows.')
    def test_case_5(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Requires Linux.')
    def test_case_6(self):
        self.assertEqual('aws'.upper(), 'AWS')
