class Dog(object):
    name = 'Jack' # class parameter

    def __init__(self, name = None):
        self.name = name # instance parameter

Jack = Dog("Zed")
print(Jack.name) # Zed

Hack = Dog()
print(Hack.name) # None

print(Dog.name) # Jack