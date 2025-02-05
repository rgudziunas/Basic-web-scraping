from bs4 import BeautifulSoup
import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

#print(soup)

#soup.find_all('table')[1]
#<table class="wikitable sortable jquery-tablesorter">
#<caption>


table = (soup.find_all('table', class_ = 'wikitable sortable')[0])
#print(soup.find_all('th'))

titles = table.find_all('th')

titles = [title.text.strip() for title in titles]

print(titles)

import pandas as pd

df = pd.DataFrame(columns=titles)
print(df)

#print(table.find_all('tr'))

rows = table.find_all('tr')

for row in rows[1:]:
    row_data = row.find_all('td')
    row_data_simplified= [data.text.strip() for data in row_data]
    #print(row_data_simplified)
    length = len(df)
    df.loc[length]=row_data_simplified

print(df)  

df.to_csv(r'C:\Users\Windows 10\Desktop\WebScraping\Output.csv', index=False)