import unittest
from unittest_basic.tax.tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_ten_percent(self):
        self.assertEqual(calc_tax(100, 0.1, 20), 10)

    def test_calc_tax_with_fourteen_percent(self):
        self.assertAlmostEqual(14, calc_tax(100, 0.14, 20))

    def test_calc_tax_with_incorrect_amount_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, '10', 0.23)

    def test_calc_tax_with_incorrect_tax_rate_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 10, '0.23')

    def test_calc_tax_negative_age(self):
        self.assertRaises(ValueError, calc_tax, 1000, 0.1, -10)

    def test_calc_tax_incorrect_age(self):
        self.assertRaises(TypeError, calc_tax, 1000, 0.1, '10')

    def test_calc_tax_age_0(self):
        self.assertRaises(ValueError, calc_tax, 1000, 0.1, 0)

    def test_calc_tax_age_18(self):
        self.assertEqual(calc_tax(100000, 0.1, 18), 5000)

    def test_calc_tax_age_1(self):
        self.assertEqual(calc_tax(100000, 0.1, 1), 5000)

    def test_calc_tax_age_18_min_calculated(self):
        self.assertEqual(calc_tax(100, 0.1, 18), 10)

    def test_calc_tax_age_1_min_calculated(self):
        self.assertEqual(calc_tax(100, 0.1, 18), 10)

    def test_calc_tax_age_65(self):
        self.assertEqual(calc_tax(100000, 0.1, 65), 10000)

    def test_calc_tax_age_19(self):
        self.assertEqual(calc_tax(100000, 0.1, 19), 10000)

    def test_calc_tax_age_66(self):
        self.assertEqual(calc_tax(100000, 0.1, 66), 8000)

    def test_calc_tax_age_66_min_calculated(self):
        self.assertEqual(calc_tax(10000, 0.1, 66), 1000)
