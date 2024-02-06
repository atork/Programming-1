#tutorial https://www.w3schools.com/python/pandas/pandas_getting_started.asp
import pandas as pd
my_data_set={
    "Autos" :["Opel","VW","Merzedes"],
    "Gewicht":[1,2,3]
}
print(my_data_set)
var=pd.DataFrame(my_data_set)
print(var)

#words with __WORD__ are attributes
print(pd.__version__)