class cars:
    def __init__(self,speed,color):
        self.__speed = speed
        self.color = color
    def set_speed(self,value):
        self.__speed = value
    def get_speed(self):
        print(self.__speed)

ford = cars (250,"Green")
BMW = cars(350,"Green")
ferrari = cars (400,"Green")

ford.get_speed()
ford.set_speed(200)
ford.get_speed()

print(ford.__dict__)



