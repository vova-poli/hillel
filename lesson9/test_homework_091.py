import unittest
from homework_091 import filter_by_string, sum_of_even, arithmetic_mean


class TestFilterByString(unittest.TestCase):

    def test_only_strings(self):
        self.assertEqual(filter_by_string(["a", "b", "c"]), ["a", "b", "c"])

    def test_mixed_types(self):
        self.assertEqual(filter_by_string(["1", 1, "b", 3.5, True, "z"]), ["1", "b", "z"])

    def test_no_strings(self):
        self.assertEqual(filter_by_string([1, 2.5, False, None]), [])

    def test_empty_list(self):
        self.assertEqual(filter_by_string([]), [])

    def test_nested_list(self):
        self.assertEqual(filter_by_string(["a", ["b"], "c"]), ["a", "c"])  # only top-level str


class TestSumOfEven(unittest.TestCase):

    def test_all_even(self):
        self.assertEqual(sum_of_even([2, 4, 6, 8]), 20)

    def test_mixed_even_odd(self):
        self.assertEqual(sum_of_even([1, 2, 3, 4, 5]), 6)

    def test_all_odd(self):
        self.assertEqual(sum_of_even([1, 3, 5, 7]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_even([-4, -3, -2, -1, 0]), -6)  # -4 + -2 + 0

    def test_empty_list(self):
        self.assertEqual(sum_of_even([]), 0)


class TestArithmeticMean(unittest.TestCase):

    def test_regular_list(self):
        self.assertAlmostEqual(arithmetic_mean([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertEqual(arithmetic_mean([42]), 42)

    def test_empty_list(self):
        self.assertEqual(arithmetic_mean([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(arithmetic_mean([-5, -15, -10]), -10.0)

    def test_floats(self):
        self.assertAlmostEqual(arithmetic_mean([1.5, 2.5, 3.5]), 2.5)

    def test_mixed_int_float(self):
        self.assertAlmostEqual(arithmetic_mean([1, 2.5, 4]), 2.5)

    def test_zeros(self):
        self.assertEqual(arithmetic_mean([0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()