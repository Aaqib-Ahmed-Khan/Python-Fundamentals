# cleaning data : it means the bad data in your data set.bad data can be empty cell, data in a wrong  format,duplicate data and wrong data

# empty cell :it will give you wrong result always,we will have to remove the rows always that contain the bad data
# loading and reading the original dataframe
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')

print(aaqib.to_string)

# here we will return a new data frame with no empty cell
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')

aaqibnew=aaqib.dropna()
print(aaqibnew.to_string) 

# if at any case you want to cahnge the original dataframe than use the implace=true argument ,it will remove the rows containing the null(nan) values
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
aaqib.dropna(inplace=True)
print(aaqib.to_string()) 

# replacing the empty value we wil use the fillna ( ) method which will use to replace the empty cell with a value
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
aaqib.fillna(130,inplace=True)
print(aaqib.to_string()) 
# to replace only the emplty value for one coloumn you need to specify the coloumn name
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
aaqib["Calories"].fillna(130,inplace=True)
print(aaqib.to_string())   

# here we can also replace the empty cell using mean (),median or mod(). 
# calculate the mean and replace the empty values with it .
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
x=aaqib["Calories"].mean()
aaqib["Calories"].fillna(x,inplace=True)
print(aaqib.to_string())

# calculate the median and replace any empty values in it..

import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
x=aaqib["Calories"].median()
aaqib["Calories"].fillna(x,inplace=True)
print(aaqib.to_string())

# median is best for market trend

# calculate the mod and replace the empty cell with it
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
x=aaqib["Calories"].mode()[0]
aaqib["Calories"].fillna(x,inplace=True)
print(aaqib.to_string())  #mostly used mode  