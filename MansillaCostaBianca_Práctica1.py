# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:37:37 2024

@author: 55194298
"""

import requests
import json
fechas = ["01-01-2024", "01-07-2024"]
datos = []
for dia in fechas:
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={dia}"
    response = requests.get(url)
    if response.status_code == 200:
       data = response.json()
       current_price_usd = data["market_data"]["current_price"]["usd"]
       current_price_eur = data["market_data"]["current_price"]["eur"]
       datos_fecha = {"fecha": dia, "usd": current_price_usd, "eur": current_price_eur}
       datos.append(datos_fecha)
    else:
        print(f"Error en datos de la fecha {dia}: código {response.status_code}")
print(json.dumps(datos, indent=4))

with open("bitcoin_historical_data.json", "w") as json_file:
    json.dump(datos, json_file, indent=4)