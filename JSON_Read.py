import json

with open ('StudentList.json') as jsonfile:
    studentData = json.load(jsonfile)

#print(studentData) #To display data in JSON file
#print(type(studentData)) #To display the type of data structure

import pandas as pd

df = pd.DataFrame(studentData,columns=['Name','Age','Class','Adress'])

#INSERTING Method 1:
'''df.loc[5] = ['Shabeer', 15, 10, 'PO Box 162272']
print(df.loc[5])# adding a row''' #WHY?

#INSERING Method 2:
'''new_row = [{'Name': 'Shabeer',
            'Age':15,
            'Class':10,
            'Adress':'PO Box 162272'}]
df = df.append(new_row, ignore_index= True)'''
#INSERING Method 3:
'''new_row = pd.DataFrame([{'Name': 'Shabeer','Age':15,'Class':10,'Adress':'PO Box 162272'}])
df = pd.concat([new_row,df],ignore_index=True)'''

#TO DELETE AT specific index:
#df.drop([0], inplace = True)

#SEARCH :
'''name_search = input("Enter the name to search")
print(df.loc[df["Name"] == name_search])'''

#SEARCH
'''name_search = input("Enter the name to search")
print(df.where(df['Name']== name_search))'''

#TO SEARCH & Delete
'''print(df)
name_search = input("Enter the name to search")
for x in df.index:
    if(df.loc[x]["Name"] == name_search):
        flag = x;
        print("Name found at Index",x)
        print(df.loc[x])
        choice = input("Delete?(Y/N)")
        if(choice == "Y"):
            df.drop([x], inplace = True)
        print(df)
    else:
        continue'''


#Search using WHERE
#print(df.where(df['Name']=='Aravindan'))





print(df) #To display the data frame

#df.to_csv('StudentList_CSV.csv')