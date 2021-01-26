class Circle(object):
    def __init__(self,  r):
        self.radius = r
    
    def compute_area(self,):
        return 3.1415*(self.radius**2)

circle = Circle(10)
print(circle.compute_area())