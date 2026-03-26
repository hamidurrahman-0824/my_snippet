import math 
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return f"Area of rectangle = {self.width*self.height}"
    def perimeter(self):
        return f"perimeter = {2*self.width+self.height*2}"
class Circle:
     
    def __init__(self,radius):
        self.radius = radius
    def area(self):
      
        return f"Area of square = {math.pi*self.radius**2}"
    def circumference(self):
        return f"circum. = {math.pi*2*self.radius}"
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h