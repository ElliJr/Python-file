import requests
from bs4 import BeautifulSoup

def search_web(query):
  url = 'https://www.google.com/search'
  params = {'q': query}
  response = requests.get(url, params=params)
  soup = BeautifulSoup(response.text, 'html.parser')
  results = soup.find_all('div', class_='r')
  for result in results:
    print(result.text)

search_web('user_input')