import bs4
import requests
import webbrowser

# Opens Google search results in separate tabs

search = input('What to search?\n')
links_num = input('How many results do you need? \n')
print('Searching...')
res = requests.get(f'https://www.google.com/search?q={search}')
res.raise_for_status()

linksSoup = bs4.BeautifulSoup(res.text, features='html.parser')
linksElems = linksSoup.select('a')

links = []
for link in linksElems:
    if '/url?q=' in link.get('href'):
        linkHref = link.get('href').split('?q=')[1].split('&sa=U')[0]
        if linkHref not in links:
            links += [linkHref]

links_filtered = []

for l in links:
    if 'wikipedia' in l:
        links_filtered += [l]
        break

for link in links:
    if 'wikipedia' in link:
        continue
    links_filtered += [link]


links_to_open = min(int(links_num), len(links_filtered))
print('Opening in the browser...')
for i in range(links_to_open):
    webbrowser.open(links_filtered[i])
print('Done.')

