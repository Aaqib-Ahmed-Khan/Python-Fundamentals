# it is a 2d structure like 2d array with table incl rows and columns
import pandas as pd
data={"cal":[200,300,400],"duration":[50,40,45]}
aaqib=pd.DataFrame(data)
print(aaqib)
# locate a specific row using attribute loc it retuetns onw or more specified row
import pandas as pd
data={"cal":[200,300,400],"duration":[40,45,50]}
aaqib=pd.DataFrame(data)
print(aaqib.loc[1])

# example of returning row 0 and 1
import pandas as pd
data={"cal":[200,300,400],"duration":[40,45,50]}
aaqib=pd.DataFrame(data)
print(aaqib.loc[[0,1]])

# name index with the index argument we can anme our own index
import pandas as pd
data={"cal":[200,300,400],"duration":[40,45,50]}
aaqib=pd.DataFrame(data,index=["day1","day2","day3"])
print(aaqib)

# print hte named index in series output
import pandas as pd
data={"cal":[200,300,400],"duration":[40,45,50]}
aaqib=pd.DataFrame(data,index=["day1","day2","day3"])
print(aaqib.loc["day2"])

# output in dataframe
import pandas as pd
data={"cal":[200,300,400],"duration":[40,45,50]}
aaqib=pd.DataFrame(data,index=["day1","day2","day3"])
print(aaqib.loc[["day2","day1"]])

# load data from csv file into  i.e data.csv

import pandas as pd
fileload= pd.read_csv('IMDB-Movie-Data.csv')
print(fileload)