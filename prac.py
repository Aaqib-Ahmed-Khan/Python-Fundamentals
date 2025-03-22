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