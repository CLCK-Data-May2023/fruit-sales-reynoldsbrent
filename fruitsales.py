# add your code here
import pandas as pd
import numpy as np

data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

df = pd.DataFrame(data)

df.index = ['2017 Sales', '2018 Sales']

df.to_csv('fruit.csv')