Names = ["Eza","Ravi","Mridul","Ragam","Fathima","Scania"]
print("Using Range/Len")
for index in range(len(Names)):
    print(index,Names[index])
print("Using ENUMERATE")
for index,name in enumerate(Names):
    print(index,name)