#https://www.w3schools.com/python/pandas/pandas_csv.asp
#The data.csv file can also be downloaded there
import pandas as pd

#pd.read_csv('data.csv') cant read the file in correctly
df = pd.read_csv('data.csv')
#.toString is needed as the csv seems not to be a String unlike the DataFrames
print(df.to_string())