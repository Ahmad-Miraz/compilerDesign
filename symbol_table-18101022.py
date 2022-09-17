import pandas as pd

df = pd.DataFrame(columns=['Name','DataType'])

def Insert(df, name, typee):
    if (name not in df.Name.values) or (typee not in df.DataType.values):
        anyword = list(name)
        asciivalue = ord(anyword[0])
        index = asciivalue%2
        indexes = df.index
        for i in range(len(indexes)):
            if(indexes[i] == index):
                asciivalue = ord(anyword[0+1])
                index = asciivalue%2
                df.loc[index] = [name,typee]
        df.loc[index] = [name,typee]

def Search(df, name):
    print( '\n',df.loc[df['Name'] == name])

def Delete(df, name):
    try:
        idxdelete = df.loc[df['Name'] == name].index[0]
        df.drop([idxdelete],axis=0,inplace=True)
        print('\n',df)
    
    except:
        print("Deleting value not found")

def Show():
    print(df)

def Update(df, name=None, New_name=None, typee=None, New_typee=None):
    if name:
        if name in df.Name.values:
            index = df.loc[df.Name == name,'Name'].index[0]
            df.loc[index,['Name']] = New_name
            df.loc[index,['Type']] = New_typee
    print(df)

def GetHashKey(df, name):
    print('The Hashkey is: ',df.loc[df['Name'] == name].index[0])

while True:
  number_of_function = int(input("\n1.Insert Function \n2.Search Function \n3.Delete Function \n4.Show Function \n5.Update Function \n6.GetHashKey Function \n7.Exit From Function \nEnter choisen any function:"))

  # For Insert
  if number_of_function == 1:
    a = input("Enter any name->")
    b = input("Enter datatype->")
    Insert(df, a, b)
  # For Search 
  if number_of_function == 2:
    s=input("Enter any name->")
    Search(df,s)  
  # For Delete
  if number_of_function == 3:
    d=input("Enter any name->")
    Delete(df, d)
  # For Show 
  if number_of_function == 4:
    print('\n', df)
  # For Update
  if number_of_function == 5:
    x=input("Enter any name->")
    y=input("Enter any new  name->")
    z=input("Enter any new type->")
    Update(df, x, y, z)
  # For Get Hash Key
  if number_of_function == 6:
    g=input("Enter any name->")
    GetHashKey(df,g)
  # For Exit from Function 
  if number_of_function == 7:
    break  
