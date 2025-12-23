import pytest
import src.shapes as shapes
import math

# Class testing comes with setup method.
# It also comes with a teardown method.
# use -s flag to display print statements


class TestCircle:

  def setup_method(self, method):
    print(f"Setting up {method}")
    self.circle = shapes.Circle(10)
  def teardown_method(self, method):
    print(f"Tearing down {method}")
    del self.circle
  
  def test_radius(self):
    assert self.circle.area() == math.pi * self.circle.radius ** 2


  def test_perimeter(self):
    result = self.circle.perimeter()
    expected = 2 * math.pi * self.circle.radius
    assert result == expected
 

  # making use of my_rectangle from conftest.py being global
  def test_not_same_area(self, my_rectangle):
    assert self.circle.area() != my_rectangle.area()