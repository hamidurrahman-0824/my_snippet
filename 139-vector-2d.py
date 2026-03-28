class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.num = tuple(x,y)
    def add(self,a,b):
        self.x +=a
        self.y +=b
        return f"({self.x,self.y})"
    def subtract(self,a,b):
        self.x -= a
        self.b -= b
        return f"({self.x,self.y})"
    def show(self):
        return f"{self.x}i + {self.y}j"
    def __repr__(self):
        return f" (x = {self.x},(y = {self.y}))"
    def modulus(self):
        return f"Modulus = {(self.x**2+self.y**2)**0.5}"
    def dotprod(self,x:tuple)->tuple:
        a,b = x
        c,d = self.num
        return (a*c,b*d)
    def is_perpendiculer(self,second_vector):
        pass
#copilot
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num = (x, y)

    def add(self, a, b):
        self.x += a
        self.y += b
        self.num = (self.x, self.y)
        return f"({self.x}, {self.y})"

    def subtract(self, a, b):
        self.x -= a
        self.y -= b
        self.num = (self.x, self.y)
        return f"({self.x}, {self.y})"

    def show(self):
        return f"{self.x}i + {self.y}j"

    def __repr__(self):
        return f"(x = {self.x}, y = {self.y})"

    def modulus(self):
        return f"Modulus = {(self.x**2 + self.y**2)**0.5}"

    def dotprod(self, other: tuple) -> float:
        a, b = other
        c, d = self.num
        return a * c + b * d

    def is_perpendiculer(self, second_vector) -> bool:
        return self.x * second_vector.x + self.y * second_vector.y == 0
