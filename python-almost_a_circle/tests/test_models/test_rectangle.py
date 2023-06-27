import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io

class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        # Runs before every test
        self.rectangle = Rectangle(4, 5, 1, 2, 10)

    def test_attributes(self):
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 1)
        self.assertEqual(self.rectangle.y, 2)
        self.assertEqual(self.rectangle.id, 10)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 20)

    def test_display(self):
        expected_output = "\n\n ####\n ####\n ####\n ####\n ####\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_output:
            self.rectangle.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_string_representation(self):
        expected_output = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(self.rectangle), expected_output)
    def test_update(self):
        self.rectangle.update(2, height=8, y=3)
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 1)  # El valor de x no debería cambiar
        self.assertEqual(self.rectangle.y, 2)
        self.assertEqual(self.rectangle.id, 2)

if __name__ == '__main__':
    unittest.main()