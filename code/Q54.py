class Shape(object):
    def __init__(self):
        pass
    
    def getArea(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def getArea(self):
        return self.length*self.length

shape = Shape()
print(shape.getArea())
square = Square(5)
print(square.getArea())