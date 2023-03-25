import requests
from bs4 import BeautifulSoup
import pprint 

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
nextpage = soup.select('.morelink')
print(nextpage[0].get('href'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext, nextpage):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None) 
        votes = subtext[idx].select('.score')

        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    

    return sort_stories_by_votes(hn)

hn2 = create_custom_hn(links, subtext, nextpage)

pprint.pprint(hn2)