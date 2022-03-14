import unittest
from parameterized import parameterized
from unittest_basic.calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_parametrized(self):
        cases = [
            (-3, -2, -5),
            (-3, 2, -1),
            (3, -2, 1),
            (3, 2, 5)
        ]
        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(self.calc.add(x, y), result)

    @parameterized.expand([
        (-3, -2, -5),
        (-3, 2, -1),
        (3, -2, 1),
        (3, 2, 5)
    ])
    def test_add_parametrized2(self, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)

    def test_sub(self):
        self.assertEqual(self.calc.sub(3, 4), -1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(3, 4), 12)

    def test_true_div(self):
        self.assertEqual(self.calc.true_div(12, 4), 3)

    def test_floor_div(self):
        self.assertEqual(self.calc.floor_div(11, 4), 2)
