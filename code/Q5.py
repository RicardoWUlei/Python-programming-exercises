class myString(object):
    def __init__(self):
        super().__init__()
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

myStringObject = myString()
myStringObject.getString()
myStringObject.printString()