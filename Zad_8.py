import requests
import argparse
from Browar import Browar

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, default=None)
args = parser.parse_args()
params = {"per_page": 20}

if args.city:
    params["by_city"] = args.city.lower()

response = requests.get(
    "https://api.openbrewerydb.org/v1/breweries",
    params=params
)
data = response.json()
lista = []
for i in data:
    lista.append(Browar(
        id=i["id"],
        name=i["name"],
        brewery_type=i["brewery_type"],
        address_1=i["address_1"],
        address_2=i["address_2"],
        address_3=i["address_3"],
        city=i["city"],
        state_province=i["state_province"],
        postal_code=i["postal_code"],
        country=i["country"],
        longitude=i["longitude"],
        latitude=i["latitude"],
        phone=i["phone"],
        website_url=i["website_url"],
        state=i["state"],
        street=i["street"]
    ))
for browar in lista:
    print(browar)
