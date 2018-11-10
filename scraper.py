from requests import get
from bs4 import BeautifulSoup
# import pandas as pd


# request content of [NORMAL] monster card [LEVEL 1-4] [ATK 0-3000] [DEF 0-3000] [ATTR WATER] [SPECIES=TYPE SEA SERPENT]
# sort = ?, rp = 100 [show 100 items], page=1 [first page]
# url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=2&sort=1&rp=100&page=1'
url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=1&starfr=1&' \
      'starto=4&pscalefr=&pscaleto=&linkmarkerfr=&linkmarkerto=&link_m=2&atkfr=0&atkto=3000&deffr=0&defto=3000&' \
      'attr=13&species=5&othercon=2&other=1&sort=1&rp=100&page=1'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

card_containers = html_soup.find_all('dl')

# List for storing scraped data
names = []
attributes = []
levels = []
types = []
atks = []
defs = []
descriptions = []

# Extract each monster card
for card in card_containers:

    # Parse name
    name = card.strong.text
    names.append(name)

    # Parse attribute
    attribute = card.find('span', class_='box_card_attribute').text.strip()
    attributes.append(attribute)

    # Parse level/rank
    level = int(card.find('span', class_='box_card_level_rank').text.strip().split(sep=' ')[1])
    levels.append(level)

    # Parse type
    card_type = card.find('span', class_='card_info_species_and_other_item').text.strip().strip('[').strip(']').\
        split(sep='/')
    types.append(card_type)

    # Parse atk points
    atk = int(card.find('span', class_='atk_power').text.strip().split(sep=' ')[1])
    atks.append(atk)

    # Parse def points
    defence = int(card.find('span', class_='def_power').text.strip().split(sep=' ')[1])
    defs.append(defence)

    # Parse card effect/description
    card_text = card.find('dd', class_='box_card_text')
    for br in card_text.find_all('br'):
        br.replace_with("\n")
    description = card_text.text.strip()
    descriptions.append(description)


# test_df = pd.DataFrame({'name': names,
#                         'attribute': attributes,
#                         'level/rank': levels,
#                         'types': types,
#                         'atk': atks,
#                         'defs': defs,
#                         'effect': descriptions})
# print(test_df.info())
# test_df