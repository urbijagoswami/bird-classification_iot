import pandas as pd
df=pd.read_csv(r"C:\Users\URBIJA GOSWAMI\Downloads\putty32.csv")
df.head()
df.columns
df.shape
new = df["name percentage"].str.split(":", n = 1, expand = True)
  
# making separate first name column from new data frame
df[" Name"]= new[0]
  
# making separate last name column from new data frame
df["percentage"]= new[1]
df.head()
df.pop("name percentage")
df.to_csv(r'C:\Users\URBIJA GOSWAMI\Downloads\file13.csv')
df1=pd.read_csv(r'C:\Users\URBIJA GOSWAMI\Downloads\file13.csv')
df1.head()
import matplotlib as plt
df1.groupby([" Name"]).sum().plot(kind='pie', y='percentage')
