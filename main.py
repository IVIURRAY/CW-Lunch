import urllib.request
from bs4 import BeautifulSoup

COST_PER_SPIN = 0.1
CREDIT = 0

URL = 'https://canarywharf.com/eating-drinking/directory/?letter=numbers'

response = urllib.request.urlopen(URL)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
all = soup.find_all('ul', {'class': 'all-list'})[0].find_all('li')


class LunchPlace:

    def __init__(self, name, href=None):
        self._name = name
        self._href = href or 'https://canarywharf.com/eating-drinking/directory/?letter=numbers'

    def name(self):
        return self._name

    def website(self):
        return self._href

    def __eq__(self, other):
        return other.name == self._name

    def __str__(self):
        return self._name

    def __hash__(self):
        return hash(self._name)

lunch_spots = []
for item in all:
    place = item.find_all('a')[0]
    link = place.get('href')
    name = place.get('title').replace('Permanent Link to ', '')

    lunch = LunchPlace(name, link) #.name()
    if lunch not in lunch_spots:
        lunch_spots.append(lunch)

from pprint import pprint
pprint(lunch_spots)

import random
def select_random_lunch_spot(lunch_spots, exluded_numbers=[]):
    number = random.randint(0, len(lunch_spots))
    if number in exluded_numbers:
        number = random.randint(0, len(lunch_spots))

    return number


selection1 = select_random_lunch_spot(lunch_spots)
selection2 = select_random_lunch_spot(lunch_spots, exluded_numbers=[selection1])
selection3 = select_random_lunch_spot(lunch_spots, exluded_numbers=[selection1, selection2])

print('\n')
print(' Random Choices '.center(45, '='))
print('Random choice 1: ', lunch_spots[selection1].name().center(30, ' '), lunch_spots[selection1].website())
print('Random choice 2: ', lunch_spots[selection2].name().center(30, ' '), lunch_spots[selection2].website())
print('Random choice 3: ', lunch_spots[selection3].name().center(30, ' '), lunch_spots[selection3].website())
