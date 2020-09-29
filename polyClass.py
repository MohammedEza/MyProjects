#This is an example of polymorphism
class UK:
    def capital():
        print("London is the capital")
    def lang():
        print("English is the language")
class Spain:
    def capital():
        print("Madrid is the capital")
    def lang():
        print("Spanish is the language")

queen = UK
zara = Spain
print("USING FOR LOOP")
for x in (queen,zara):
    x.capital()
    x.lang()
print("USING FUNCTION")
def printinfo (obj):
    obj.capital()
    obj.lang()
printinfo(queen)
printinfo(zara)
