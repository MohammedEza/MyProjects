car = ["BMW", "Benz", "Audi", "Jeep", "Toyota"]
engine = ["IC","Electric","Hybrid"]
car.extend(engine)
print(car)
engine.append("Fuel cell")
print(engine)


print(car.count("IC"))
car.sort()
print(car)
print(car.index("BMW"))
car.pop()
print (car)
car.remove("Hybrid")
print(car)
del car
#print (car)