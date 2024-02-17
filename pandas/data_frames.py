#tutorial https://www.w3schools.com/python/pandas/pandas_series.asp
import pandas as pd

data={
    "calorien":[69,420,187],
    "duration":[10,20,30]
}
var= pd.DataFrame(data)
print(var)