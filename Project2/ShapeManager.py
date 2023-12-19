class ShapeManager:
    def init(self):
        self.shapes = []

    def create_rectangle(self, length, width):
        rectangle = Rectangle(length, width)
        self.shapes.append(rectangle)
        return rectangle

    def create_circle(self, radius):
        circle = Circle(radius)
        self.shapes.append(circle)
        return circle

    def remove_shape(self, shape):
        if shape in self.shapes:
            self.shapes.remove(shape)
            print("Shape removed.")
        else:
            print("Shape not found.")

    def display_all_shapes_info(self):
        for shape in self.shapes:
            shape.display_info()
            print(f"Area: {shape.calculate_area()}, Perimeter: {shape.calculate_perimeter()}")
            print("-" * 20)
manager = ShapeManager()