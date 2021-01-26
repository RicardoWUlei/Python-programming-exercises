class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self,):
        return self.length * self.width
    
rect = Rectangle(10, 10)
print(rect.compute_area())