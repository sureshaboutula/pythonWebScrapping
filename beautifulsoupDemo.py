import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
x = soup.find('div')
y = soup.find_all('div')
z = soup.find_all('div', class_='col-md-12')
# print(z)
#print(soup.find_all('p', class_ = 'lead'))
# print(soup.find('p', class_ = 'lead'))
# print(soup.find('p', class_ = 'lead').text.strip())
#print(soup.find_all('th'))
#print(soup.find_all('td'))
print(soup.find('th').text.strip())
print(soup.find_all('th')[0].text.strip())
print(soup.find_all('th')[1].text.strip())
print(soup.find_all('th')[2].text.strip())