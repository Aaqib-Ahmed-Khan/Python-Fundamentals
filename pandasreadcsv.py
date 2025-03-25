#  read csv files (comma seperated file it is a simple way to store the big and biggest data sets.csv files conains plain text

# loading the csv into dataframe
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())