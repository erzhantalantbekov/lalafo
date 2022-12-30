from bs4 import BeautifulSoup 
from requests import get
import time
import random

url = 'https://lalafo.kg/kyrgyzstan/transport?page='
cars = []
count = 1
while count <= 5:
    url = 'https://lalafo.kg/kyrgyzstan/transport?page=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser1')

    cars_data = html_soup.find_all('div', class_="AdTileHorizontalMainInfo")
    if cars_data != []:
        cars.extend(cars_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1
    
print(len(cars))
print(cars[0])
print()
n = int(len(cars)) - 1
count = 0
while count <= 5:  # count <= n
    info = cars[int(count)]
    price = info.find('span',{"class":"international-price"}).text
    title = info.find('a',{"class":"dTileHorizontalTitle"}).text
    print(title, ' ', price)
    count += 1