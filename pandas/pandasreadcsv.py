#  read csv files (comma seperated file it is a simple way to store the big and biggest data sets.csv files conains plain text

# loading the csv into dataframe with to_string
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())

# loading the csv into dataframe without to_string
import pandas as pd
df=pd.read_csv('data.csv')
print(df)  #shows first five and last five

# max rows :you can check your system's maximumrows with :
import pandas as pd 
print(pd.options.display.max_rows)

# yes we can increase the maximum number of roes to dispplay the enire dataframe

import pandas as pd
pd.options.display.max_rows=170  #thisis not okay way to do 
df=pd.read_csv('data.csv')
print(df)   