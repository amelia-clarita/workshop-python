import pandas as pd
import io
import requests

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

data_negara = requests.get(url).content
read_data = pd.read_csv(io.StringIO(data_negara.decode('utf-8')))
print(read_data)