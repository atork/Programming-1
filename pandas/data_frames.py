#tutorial https://www.w3schools.com/python/pandas/pandas_series.asp
#https://www.w3schools.com/python/pandas/pandas_dataframes.asp
import pandas as pd
#inputting multiple columns can also be just one
#All one index or multiple?
data={
    "calorien":[69,420,187],
    "duration":[10,20,30]
}
#loads dict into DataFrame object
var= pd.DataFrame(data)
print(var)

#able to output specififc row with DataFrame object function and index num
print(var.loc[0])
#multiple row can be an output when index is an array of index nums
print(var.loc[[1,2]])