import unittest
from rectangles import Rectangle

class TestCubes(unittest.TestCase):
    def test_init(self):
        c = Rectangle(5, 3, 10)
        self.assertEqual(c.length, 5) 
        self.assertEqual(c.width, 3) 
        self.assertEqual(c.height, 10)

    def test_init_raise(self):
        with self.assertRaises(ValueError):
            c = Rectangle('Length', (1, 2, 3), {4: 5})

    def test_negative_value(self):
        with self.assertRaises(ValueError) as context:
            c = Rectangle(-1, 2, 6)

    def test_volume_calculation(self):
        c = Rectangle(5, 4, 7)
        self.assertEqual(c.calculate_volume(), 140) 

if __name__ == "__main__":
    unittest.main()