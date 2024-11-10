import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
# world_table = soup.find('table')
# print(world_table.text.strip())

table = soup.find_all('table')[0]
# print(table)
world_titles = table.find_all('th')
# print(world_titles)
world_table_titles = [world_title.text.strip() for world_title in world_titles]
# print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)
# print(df)

columns_data = table.find_all('tr')[1:]
# print(column_data)
for row in columns_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print(individual_column_data)

    length = len(df)
    df.loc[length] = individual_row_data

#print(df)
df.to_csv(r'C:\Users\0G3425649\PycharmProjects\pythonWebScrapping\Companies.csv', index=False)




