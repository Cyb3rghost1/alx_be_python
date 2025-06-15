# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_mixed_signs(self):
        self.assertEqual(self.calc.subtract(-5, 5), -10)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 3), -3)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -6), 18)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-3, 7), -21)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 100), 0)

    # --- Division Tests ---
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-8, -2), 4)

    def test_division_mixed_signs(self):
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_result_type(self):
        self.assertIsInstance(self.calc.divide(9, 2), float)

if __name__ == "__main__":
    unittest.main()
