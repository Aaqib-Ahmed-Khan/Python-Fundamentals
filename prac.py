# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Load the CSV file
# pd.set_option("display.max_rows", None)

# # Remove column limit (show all columns)
# pd.set_option("display.max_columns", None)

# # Remove width restriction (prevent line breaking)
# pd.set_option("display.width", None)

# # Load dataset
# data = pd.read_csv(r"D:\Python\pandas\IMDB-Movie-Data.csv")

# # Print full dataset
# print(data) 

# # Alternative: Save to a CSV file if the output is too long
# data.to_csv("output.csv", index=False)  # Saves the dataset in 'output.csv'
# print("Dataset saved to output.csv")
import pandas as pd
# print(pd.__version__) 
aaqib=[1,2,3,4]
aaqibnew=pd.Series(aaqib)
print(aaqibnew) 

# with create label you can create youe own label
import pandas as pd
aaqib=[1,2,3]
aaqibnew=pd.Series(aaqib,index=["x","y","z"])
print(aaqibnew)

# creating  pandas series from dictionary
import pandas as pd
courses={"day1":1,"day2":2,"day3":3,}
aaqibnew=pd.Series(courses)
print(aaqibnew)
#  now printng only day 1 and day2
import pandas as pd
courses={"day1":1,"day2":2,"day3":3}
aaqibnew=pd.Series(courses,["day1","day2"])
print(aaqibnew)

# 1 dimensional finished now moving to 2 dimensional
# dataframs: data sets in pandas are usually multidmensional tables and they are called dataframes 
# dataframes is whole table and previously we were working on just coloum in series 
import pandas as pd
aaqib ={"courses":[1,2,3],"times":[10,20,30]}
aaqibnew=pd.DataFrame(aaqib)
print(aaqibnew)
# now after this ypu se its good looking and indexing also came by default
