# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:55:20 2024

@author: 55194298
"""
import requests
from bs4 import BeautifulSoup

# Scrapear propiedades
def scrape_properties(city_url):
    properties = []
    response = requests.get(city_url)
    
    #if response.status_code != 200:
    #    print(f"Error al acceder a {city_url}: {response.status_code}")
    #    return properties

    soup = BeautifulSoup(response.text, 'html.parser')
    property_cards = soup.find_all('div', class_='listingCard', limit=10)  

    for card in property_cards:
          
        price = card.find('div', class_='precios d-flex').text.strip() if card.find('div', class_='lc-price') else 'N/A'
        info_tam = card.find('div', class_='details-info').text.strip() if card.find('div', class_='lc-typologyTag') else 'N/A'
        location = card.find('div', class_='localidad_p').text.strip() if card.find('strong', class_='lc-location') else 'N/A'
        link = card.find('a')['href'] if card.find('a') else 'N/A'

        properties.append({

            'precio': price,
            'información': info_tam,
            'habitaciones': location,
            'link': link
        })

    return properties

cities = {
    'Montevideo': "https://www.casasymas.com.uy/propiedades/venta/montevideo",
    'Artigas': "https://www.casasymas.com.uy/propiedades/venta/artigas",
    'Salto': "https://www.casasymas.com.uy/propiedades/venta/salto"
}

   
all_properties = {}
for city, url in cities.items():
    print(f"Scrapeando propiedades en {city}...")
    properties = scrape_properties(url)
    all_properties[city] = properties

# Imprimir resultados
for city, properties in all_properties.items():
    print(f"\nPropiedades en {city}:")
    for prop in properties:
        print(prop)
