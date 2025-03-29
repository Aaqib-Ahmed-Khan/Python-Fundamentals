# removing the duplicate values : 1st you need to discover the duplcate vslues via duplicate()method 


# loading and reading the original dataframe
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
print(aaqib.to_string()) 

# return true for every row that is duplicate otherwise return false:
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
print(aaqib.duplicated()) 