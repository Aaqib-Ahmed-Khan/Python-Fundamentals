# wrong Data: its only a wrong data

# loading and reading the original dataframe
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
print(aaqib.to_string())

# here we will set "duration" =45 in row 7:
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
aaqib.loc[7,'Duration']=45
print(aaqib.to_string())

# for larger data sets:now here we will loop through all the values in duration column if the value is higher than 120 then set it to 120
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
for i in aaqib.index:
    if aaqib.loc[i,"Duration"] >120:
        aaqib.loc[i,"Duration"]=120
print(aaqib.to_string())

# we can also remove the rows for wring data in larger data sets
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
for i in aaqib.index:
    if aaqib.loc[i,"Duration"] > 120:
        aaqib.drop(i,inplace=True)
print(aaqib.to_string())