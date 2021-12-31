#IMPORT PACKAGES
import pandas as pd

#LOAD DATA
url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/default.csv"
data=pd.read_csv(url)

#view first six rows of dataset
print(data[0:6])