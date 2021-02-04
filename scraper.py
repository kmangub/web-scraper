import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Loch_Ness_Monster'

def get_citations_needed_count(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find(id = 'mw-content-text')
    citation_count = result.find_all('a', title="Wikipedia:Citation needed" )
    return len(citation_count)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_count = soup.find_all('a', title="Wikipedia:Citation needed")
    passages = []
    for passage in citation_count:
        passages.append(passage.find_parents('p')[0].text)
        # print(passage.find_parents('p'))
    # print(passages)
    show_passages = '\n'.join(passages)
    return show_passages

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))
# get_citations_needed_report(url)