from shape import Shape
from rectangle import Rectangle
from circle import Circle
from shapeManager import ShapeManager

manager = ShapeManager()

rectangle1 = manager.create_rectangle(5, 10)
circle1 = manager.create_circle(7)
rectangle2 = manager.create_rectangle(3, 6)
circle2 = manager.create_circle(4)
manager.display_all_shapes_info()
manager.remove_shape(rectangle1)
manager.display_all_shapes_info()