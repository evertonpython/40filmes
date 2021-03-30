from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = "https://laparola.com.br/os-40-melhores-filmes-animados-da-disney"
 
response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

tags = soup.find_all('strong')

for tag in tags:
	dataframe = pd.DataFrame(tags)
	print(dataframe)
