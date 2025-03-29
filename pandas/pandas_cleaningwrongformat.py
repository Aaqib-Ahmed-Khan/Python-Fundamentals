# data in a wrong format :to fix this problem there are two ways:removing the rows or convert all teh cells in the same format
import pandas as pd
aaqib = pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
print(aaqib.to_string) 

# lets try to convert all the cells in the date columns into dates.via tp_datetime()
import pandas as pd
aaqib=pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
aaqib["Date"]=pd.to_datetime(+aaqib['Date'], errors='coerce')
print(aaqib.to_string())


# here now we will remove the rows with a null value in the date column
aaqib=pd.read_csv(r'D:\Python\pandas\dirtydata.csv')
aaqib["Date"]=pd.to_datetime(aaqib['Date'], errors='coerce')
aaqib.dropna(subset=['Date'],inplace=True)
print(aaqib.to_string())
