class MyClass :
    brand = "Lamborgini"
    course = "Speed Track"
    def __init__(self):
        self.course = course
    def getinfo(self):
        print("My brand is ", self.brand)
MyCar = MyClass
MyCar.getinfo(MyCar)
