import pandas as pd
import matplotlib as plt
# reads the csv file while skipping the first row and 'names' assigns variable names manually.
df=pd.read_csv(r"path and name of the putty file", skiprows=1, names=['name percentage'])
df.head()
df.shape 
#splitting the values of name percentage column
new = df["name percentage"].str.split(":", n = 1, expand = True)
# making separate name column from new data frame
df["Name"]= new[0]
# making separate percentage column from new data frame
df["percentage"]= new[1]
df.head()
#delete the name percentage column
df.pop("name percentage")
#save the edited csv as a new file
df.to_csv(r'new csv name and path')
df1=pd.read_csv(r'new csv name and path')
df1.head()
#plotting the pie chart
df1.groupby(["Name"]).sum().plot(kind='pie', y='percentage')
