import unittest
from rhombus import Rhombus

class TestRhombus(unittest.TestCase):
    def test_valid_angles(self):
        r = Rhombus(5, 60)
        self.assertEqual(r.angle_b, 120)

    def test_auto_update_angle_b(self):
        r = Rhombus(5, 70)
        r.angle_a = 40
        self.assertEqual(r.angle_b, 140)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Rhombus(0, 60)

    def test_invalid_angle_a(self):
        with self.assertRaises(ValueError):
            Rhombus(5, 180)

    def test_set_angle_b_directly(self):
        r = Rhombus(5, 60)
        with self.assertRaises(AttributeError):
            r.angle_b = 90

if __name__ == '__main__':
    unittest.main()