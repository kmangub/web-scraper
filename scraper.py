import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Loch_Ness_Monster'

response = requests.get(url)

# print(response)
# output: <Response [200]>

content = response.content
# print(content)

soup = BeautifulSoup(content, 'html.parser')
# print(soup)
# print(soup.prettify())

result = soup.find(id = 'mw-content-text')
# print(result)


def get_citations_needed_count(url):
    citation_count = result.find_all('a', title="Wikipedia:Citation needed" )
    print(len(citation_count))

def get_citations_needed_report(url):
    pass

get_citations_needed_count(url)