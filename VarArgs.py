def contacts(a=7,*number,**phonebook):
    print("My fav number is ", a)
    for num in number:
        print (num)
    for name,id in phonebook.items():
        print(name,id)

contacts(7,1,2,3,4,5,jane=555,ravi=111,eza=999)