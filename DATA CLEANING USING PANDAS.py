#importing the pandas libraries
import pandas as pd

#reading the csv file from the local machine
df=pd.read_csv("Customer-Call-List.csv")

#dropping all columns having null values
df.dropna(how='all',axis=1,inplace=True)

#checking the data type
df.dtypes

#deleting the unwanted column
df.pop('Not_Useful_Column')

#filling the null values and checking their count
df=df.fillna('')
df.isna().sum()

#replacing values with the good format 
df['Paying Customer']=df['Paying Customer'].replace({'Y':'Yes','N':'No'})
df['Do_Not_Contact']=df['Do_Not_Contact'].replace({'Y':'Yes','N':'No'})

#dropping the duplicates
df=df.drop_duplicates()

#stripping the unwanted characters in the data
df['Last_Name']=df['Last_Name'].str.strip('..._/') #we can also use this df['Last_Name']=df['Last_Name'].str.strip('123._/')

#manupulating the data in the phone number column to give structured data
df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
df['Phone_Number']=df['Phone_Number'].apply(lambda x:str(x))
df['Phone_Number']=df['Phone_Number'].apply(lambda x:x[0:3]+'-'+x[3:6]+'-'+x[6:10])
df['Phone_Number']=df['Phone_Number'].str.replace('nan--','')
df['Phone_Number']=df['Phone_Number'].str.replace('Na--','')
df['Phone_Number']=df['Phone_Number'].str.replace('--','')


#categorising the address column
df[["Street Address","State","Zipcode"]]=df['Address'].str.split(',',2,expand=True)

#removing the null valued row using the for loop
df=df.fillna('')
for x in df.index:
    if df.loc[x,"Do_Not_Contact"]=='Yes':
        df.drop(x,inplace=True)
for x in df.index:
    if df.loc[x,"Phone_Number"]=='':
        df.drop(x,inplace=True)

#reseting the index of the data 
df=df.reset_index(drop=True)
df
