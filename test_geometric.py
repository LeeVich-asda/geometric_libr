import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rect_area, perimeter as rect_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircle(unittest.TestCase):
    
    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)
    
    def test_circle_area_normal(self):
        self.assertAlmostEqual(circle_area(3), 28.27431, places=5)
    
    def test_circle_area_large(self):
        self.assertAlmostEqual(circle_area(10), 314.159, places=3)
    
    def test_circle_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)
    
    def test_circle_perimeter_normal(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.849539999999998, places=5)
    
    def test_circle_perimeter_large(self):
        self.assertAlmostEqual(circle_perimeter(10), 62.8318, places=3)


class TestSquare(unittest.TestCase):
    
    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)
    
    def test_square_area_normal(self):
        self.assertEqual(square_area(4), 16)
    
    def test_square_area_fractional(self):
        self.assertAlmostEqual(square_area(2.5), 6.25, places=2)
    
    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)
    
    def test_square_perimeter_normal(self):
        self.assertEqual(square_perimeter(4), 16)
    
    def test_square_perimeter_fractional(self):
        self.assertAlmostEqual(square_perimeter(2.5), 10.0, places=1)


class TestRectangle(unittest.TestCase):
    
    def test_rectangle_area_zero(self):
        self.assertEqual(rect_area(10, 0), 0)
        self.assertEqual(rect_area(0, 10), 0)
    
    def test_rectangle_area_normal(self):
        self.assertEqual(rect_area(3, 4), 12)
    
    def test_rectangle_area_square(self):
        self.assertEqual(rect_area(5, 5), 25)
    
    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rect_perimeter(0, 10), 20)
        self.assertEqual(rect_perimeter(10, 0), 20)
    
    def test_rectangle_perimeter_normal(self):
        self.assertEqual(rect_perimeter(3, 4), 14)
    
    def test_rectangle_perimeter_square(self):
        self.assertEqual(rect_perimeter(5, 5), 20)


class TestTriangle(unittest.TestCase):
    
    def test_triangle_area_zero(self):
        self.assertEqual(triangle_area(0, 10), 0)
        self.assertEqual(triangle_area(10, 0), 0)
    
    def test_triangle_area_normal(self):
        self.assertEqual(triangle_area(6, 4), 12.0)
    
    def test_triangle_area_right_triangle(self):
        self.assertEqual(triangle_area(5, 8), 20.0)
    
    def test_triangle_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 1, 2), 3)
        self.assertEqual(triangle_perimeter(1, 0, 2), 3)
        self.assertEqual(triangle_perimeter(1, 2, 0), 3)
    
    def test_triangle_perimeter_normal(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    
    def test_triangle_perimeter_equilateral(self):
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)


if __name__ == '__main__':
    unittest.main()