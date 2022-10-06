from __future__ import annotations # for type hinting with classes and |-operators
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from math import pi, dist

class Shape: # super class of geometrical shapes
    """Super class of geometrical shapes: Circle, Rectangle, Sphere, Cuboid"""
    def __init__(self,  x: (int | float) = 0, 
                        y: (int | float) = 0) -> None:

        self.x = x # x-coordinate of shape, default 0
        self.y = y # y-coordinate of shape, default 0

    # ----- Properties -----
    @property
    def x(self) -> (int | float):
        """x-position of shape"""
        return self._x
    
    @x.setter
    def x(self, value: (int | float)):
        self._x = self.check_coordinate(value) # error handling through check_coordinate method

    @property
    def y(self) -> (int | float):
        """y-position of shape"""
        return self._y
    
    @y.setter
    def y(self, value: (int | float)):
        self._y = self.check_coordinate(value) # error handling through check_coordinate method

    # ----- Error handling -----
    def check_coordinate(self, value: (int | float)) -> (int | float):
        """Error handling method for all coordinate values"""
        if not isinstance(value, (int, float)): # value is not int or float:
            raise TypeError(f"Coordinate must be a number, not {type(value).__name__}")
        return value # if all checks have been passed

    def check_measurement(self, value: (int | float)) -> (int | float):
        """Error handling method for all measurement values"""
        if not isinstance(value, (int, float)): # value is not int or float:
            raise TypeError(f"Measurement must be a number, not {type(value).__name__}")
        if value <= 0: # value is not greater than 0:
            raise ValueError(f"Value must be over 0, not {value}")
        return value # if all checks have been passed

    # ----- Operator overloading for Shape class -----
    def __eq__(self, other: Shape) -> bool:
        """Override of equal (==) operator for all shapes"""
        return self.area == other.area

    def __lt__(self, other: Shape) -> bool:
        """Override of lesser than (<) operator for all shapes"""
        return self.area < other.area
            
    def __gt__(self, other: Shape) -> bool:
        """Override of greater than (>) operator for all shapes"""
        return self.area > other.area

    def __le__(self, other: Shape) -> bool:
        """Override of lesser or equal (<=) operator for all shapes"""
        return self.area <= other.area

    def __ge__(self, other: Shape) -> bool:
        """Override of greater or equal (>=) operator for all shapes"""
        return self.area >= other.area

    # ----- Other methods -----
    def translate(self, x: (int | float) = 0, y: (int | float) = 0) -> None:
        self.x += x
        self.y += y

    # ----- String representation -----
    def __repr__(self) -> str:
        return f"Shape(x_pos = {self.x}, y_pos = {self.y})"

    def __str__(self) -> str:
        return f"Shape with x: {self.x}, y: {self.y}"

class Circle(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Circle, sub-class of Shape"""
    def __init__(self,  radius: (int | float) = 1, 
                        x_pos:  (int | float) = 0, 
                        y_pos:  (int | float) = 0) -> None:

        super().__init__(x_pos, y_pos) # x and y coordinates handled in super class
        self.radius = radius # radius of circle, default 1

    # ----- Properties -----
    @property
    def radius(self) -> (int | float):
        """Radius of circle"""
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        self._radius = self.check_measurement(value)  # error handling through check_measurement method

    @property
    def area(self) -> (int | float):
        """Area of circle"""
        return pi * self.radius ** 2

    @property
    def circumference(self) -> (int | float):
        """Circumference of circle"""
        return 2 * pi * self.radius

    # ----- Other methods -----
    def is_unit_circle(self) -> bool:
        """Checks if Circle is a unit circle (circle with radius 1 centered in origo)"""
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def contains_point(self, x: (int | float), y: (int | float)) -> bool:
        """Check if circle contains a given point"""
        distance = dist((self.x, self.y), (x, y)) # calculate euclidean distance between center point of self and input point
        if distance <= self.radius: # if distance to input point is less than or equal to radius:
            return True # point is within circle (including on circle border)
        else:
            return False # point is outside circle

    def plot(self, ax): # TODO type hinting
        """Adds Circle patch object to ax"""
        ax.add_patch(patches.Circle((self.x, self.y), self.radius))
        return ax

    # ----- String representation -----
    def __repr__(self) -> str:
        """"Describes self as a string"""
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"

    def __str__(self) -> str:
        """Describes self as a string for printing"""
        return f"Circle in position x: {self.x}, y: {self.y}, with radius: {self.radius}, area: {self.area}, circumference: {self.circumference}"

class Rectangle(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Rectangle, sub-class of Shape"""
    def __init__(self,  width:  (int | float) = 1, 
                        height: (int | float) = 1, 
                        x:      (int | float) = 0, 
                        y:      (int | float) = 0) -> None:

        super().__init__(x, y)  # x and y coordinates handled in super class
        self.width = width      # width of rectangle,   default 1
        self.height = height    # height of rectangle,  default 1

    # ----- Properties -----
    @property
    def width(self) -> (int | float):
        """Width of rectangle"""
        return self._width

    @width.setter
    def width(self, value: (int | float)):
        self._width = self.check_measurement(value)  # error handling through check_measurement method

    @property
    def height(self) -> (int | float):
        """Height of rectangle"""
        return self._height

    @height.setter
    def height(self, value: (int | float)):
        self._height = self.check_measurement(value)  # error handling through check_measurement method

    @property
    def area(self) -> (int | float):
        """Area of rectangle"""
        return self.width * self.height

    @property
    def perimeter(self) -> (int | float):
        """Perimeter of rectangle"""
        return self.width * 2 + self.height * 2

    # ----- Other methods -----
    def is_equilateral(self) -> bool:
        """Checks if Rectangle is a square"""
        if self.width == self.height:
            return True
        else:
            return False

    def contains_point(self, x: (int | float), y: (int | float)) -> bool:
        """Check if rectangle contains a given point"""
        width_range, height_range = self.width / 2, self.height / 2 # distance from rectangle center that point needs to be within

        if  (self.x - width_range <= x <= self.x + width_range 
        and self.y - height_range <= y <= self.y + height_range): # if x and y within distance:
            return True # point is within rectangle (including on rectangle border)
        else:
            return False # point is outside rectangle

    def plot(self, ax): # TODO type hinting
        """Adds Rectangle patch object to ax"""
        ax.add_patch(patches.Rectangle((self.x, self.y), self.width, self.height))
        return ax

    # ----- String representation -----
    def __repr__(self) -> str:
        """"Describes self as a string"""
        return f"Rectangle(x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height})"

    def __str__(self) -> str:
        """Describes self as a string for printing"""
        return f"Rectangle in position x: {self.x}, y: {self.y}, with width: {self.width}, height: {self.height}, area: {self.area}, perimeter: {self.perimeter}"

class Sphere(Circle): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Sphere, sub-class of Shape"""
    def __init__(self,  radius: (int | float) = 1, 
                            x:  (int | float) = 0, 
                            y:  (int | float) = 0, 
                            z:  (int | float) = 0) -> None:

        super().__init__(radius, x, y)  # x and y coordinates handled in super class
        self.z = z              # z-coord of sphere, default 0

    # ----- Properties -----
    @property
    def z(self) -> (int | float):
        """z-position of shape"""
        return self._z
    
    @z.setter
    def z(self, value: (int | float)):
        self._z = self.check_coordinate(value) # error handling through check_coordinate method

    @property
    def area(self) -> (int | float):
        """Surface area of shape"""
        return 4 * super().area
    
    @property
    def volume(self) -> (int | float):
        """Volume area of shape"""
        return (4/3) * pi * self.radius**3

    # ----- Methods -----
    def is_unit_shape(self) -> bool:
        if super().is_unit_circle() and self.z == 0:
            return True
        else:
            return False

    def translate(self, x: (int | float) = 0, y: (int | float) = 0, z: (int | float) = 0):
        super().translate(x, y)
        self.z += z

    def contains_point(self, x: (int | float), y: (int | float), z: (int | float)) -> bool:
        if dist((self.x, self.y, self.z), (x, y, z)) <= self.radius:
            return True
        else:
            return False

    # TODO plot

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__
    
class Cuboid(Rectangle): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Cuboid, sub-class of Shape"""
    def __init__(self,  width:  (int | float) = 1, 
                        height: (int | float) = 1, 
                        length: (int | float) = 1, 
                        x:      (int | float) = 0, 
                        y:      (int | float) = 0, 
                        z:      (int | float) = 0) -> None:

        super().__init__(width, height, x, y)  # width, height, and x, y coordinates handled in super class
        self.length = length    # length of cuboid,   default 1
        self.z = z              # z-coord of cuboid,  default 0

    # ----- Properties -----
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        self._length = self.check_measurement(value) # error handling through check_measurement method
    
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = self.check_coordinate(value) # error handling through check_coordinate method

    @property
    def area(self):
        return 2 * (self.width * self.height + self.height * self.length + self.length * self.width)

    @property
    def volume(self):
        return self.width * self.height * self.length

    @property
    def perimeter(self):
        return (self.width * 4) + (self.height * 4) + (self.length * 4)

    # ----- Methods -----
    def is_equilateral(self):
        """Checks if Cuboid is a Cube"""
        if self.width == self.height and self.width == self.length:
            return True
        else:
            return False

    def translate(self, x: (int | float) = 0, y: (int | float) = 0, z: (int | float) = 0) -> None:
        super().translate(x, y) # TODO better to calculate all here?
        self.z += z

    def contains_point(self, x: (int | float), y: (int | float), z: (int | float)) -> bool:
        length_range = self.length / 2
        if super().contains_point(x, y) and self.z - length_range <= z <= self.z + length_range:
            return True
        else:
            return False

    # TODO plot

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__