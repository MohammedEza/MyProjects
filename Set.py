students = set(("Eza","Scania","Bilal","Ragam"))
print(type(students))
for x in students:
    print (x)
print(len(students))
students.add("Mohammed")
students.update(["lewis","nico"])
print(students)
students.remove("lewis")
print (students)
students.clear()
print (students)
#del students
#print(students)