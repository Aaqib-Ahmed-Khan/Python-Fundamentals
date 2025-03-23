# it is a 2d structure like 2d array with table incl rows and columns
import pandas as pd
data={"cal":[200,300,400],"duration":[50,40,45]}
aaqib=pd.DataFrame(data)
print(aaqib)
# lcoate a specific row usjing attribute loc it retuetns onw or more specified row
import pandas as pd
data={"cal":[200,300,400],"duration":[40,45,50]}
aaqib=pd.DataFrame(data)
print(aaqib.loc[1])