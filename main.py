import numpy as np
import pandas as pd

#reading test file
data_initial = pd.read_csv('./files/train.csv')
#Creating a dataset without Id column
data = data_initial.drop(['Id'],axis=1)

#sort by price
print(data.sort_values(by=['SalePrice'],ascending=False))

#looking for number of missing values in all columns
#print(data.isnull().sum().sort_values(ascending=False).head(27))
