from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        print(f"Circle - Radius: {self.radius}")