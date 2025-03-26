# big data sets are normally stored and extracted as json. json is a plain text but it  has  a format of an object.
# loading the json into a dataframe:
import pandas as pd 
aaqib=pd.read_json('data.js')
print(aaqib.to_string())

# dictionary as a json if json code is not in a file but in ia a python dictionary then you can do all below
import pandas as pd 
data={"Duration":
      {"0":60,
       "1":60,
       "2":60,
       "3":60,
       "4":45,
       "5":45,
       "5":60},
    "Pulse":{
       "0":110,
       "1":117,
       "2":103,
       "3":109,
       "4":117,
       "5":102,},
    "Maxpulse":{
       "0":130,
       "1":145,
       "2":135,
       "3":175,
       "4":148,
       "5":127},
    "Calories":{
       "0":409.1,
       "1":479.0,
       "2":340.0,
       "3":282.4,
       "4":406.0,
       "5":300.5,
       }
       }
aaqibnew=pd.DataFrame(data)
print(aaqibnew)