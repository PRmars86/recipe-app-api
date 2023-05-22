"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """Test add two numbers"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtract numbers"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, -5)
