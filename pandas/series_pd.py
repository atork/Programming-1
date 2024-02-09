#tutorial https://www.w3schools.com/python/pandas/pandas_series.asp
from operator import index
import pandas as pd

a=[1, 7,3]
#panda series is column with index on the far left
var=pd.Series(a) 
print(var)   

#direct access through index
print("")
print(var[0])
print("")

#abel to replace standart num index with any key
var1= pd.Series(a,index=["x","y","z"])
print(var1)

#same direct access with new index
print("")
print(var1["x"])
print("")

#directly assigns new index matched with values
calories ={"day1": 420,"day2": 380,"day3":390}

var =pd.Series(calories)

print(var)

print("")
#when wanting only certain values from list input index keys as list
var =pd.Series(calories, index=["day1","day2"])

print(var)