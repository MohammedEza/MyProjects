mycar = { "brand": "Mercedes",
          "Fuel": "Petrol",
          "Engine": "V6 Turbo",
          "year": 2017

          }
print(type(mycar))
print(mycar)
print(len(mycar))
mycar["year"] = 2019
print(mycar)
#for x in mycar :
   #print(x)
print(mycar["year"])
print(mycar.keys())
print(mycar.values())
mycar.update({"color":"Red"})
print(mycar)
mycar.pop("color")
print(mycar)
mycar.clear()
print(mycar)