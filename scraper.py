from requests import get
from bs4 import BeautifulSoup
import re
### still have to fix multiple types, -> [machine/union/effect] 3 types
#find correct URL, distinguished between monster, spell, trap
def findurl(input):
    if input == 1:
            url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=1' #type 1 - monster
    elif input == 2:
        url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=2' #type 2 - spell
    else:
        url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=3' #type 3 - trap

    return url
input = 1
#get text from url
url = findurl(input)
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
card_containers = html_soup.find_all('dl')

# List for storing scraped data
names = []
attributes = []
levels = [] # if spell or trap, put space
types_0 = [] #normal,continuous, effect,etc.
types_1 = [] #insect,beast, spell/trap = ''
atks = [] #if spell or trap, put space
defs = [] #if speel or trap, put space
descriptions = []

# Extract each monster card
for card in card_containers:
    # declare name, attribute, level, type, atk, def, description
    name = card.find('span', class_='card_status').text.strip()
    attribute = card.find('span', class_='box_card_attribute').text
    description = card.find('dd', class_='box_card_text').text.strip()

    if input == 1:
        level = int(card.find('span', class_='box_card_level_rank').text.strip().split(sep=' ')[1])
        card_type_0 = card.find('span', class_='card_info_species_and_other_item').text.strip().strip('[').strip(']')\
        .split(sep='/')[0].strip()
        card_type_1 = card.find('span', class_='card_info_species_and_other_item').text.strip().strip('[').strip(']')\
        .split(sep='/')[1].strip()
        atk = int(card.find('span', class_='atk_power').text.strip().split(sep=' ')[1])
        defence = int(card.find('span', class_='def_power').text.strip().split(sep=' ')[1])

    else:
        level =''
        card_type_0 = card.find('span', class_='box_card_effect').text.strip()
        card_type_1 = ''
        atk =''
        defence =''

    #append to respective array
    names.append(name)
    print(name)
    attributes.append(attribute)
    print(attribute)
    levels.append(level)
    print(level)
    types_0.append(card_type_0)
    print(card_type_0)
    types_1.append(card_type_1)
    print(card_type_1)
    atks.append(atk)
    print(atk)
    defs.append(defence)
    print(defence)
    descriptions.append(description)
    print(description)



# test_df = pd.DataFrame({'name': names,
#                         'attribute': attributes,
#                         'level/rank': levels,
#                         'types': types,
#                         'atk': atks,
#                         'defs': defs,
#                         'effect': descriptions})
# print(test_df.info())
# test_df
