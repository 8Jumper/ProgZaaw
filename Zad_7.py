import requests
import argparse

class Browar:
        def __init__(self, id:str, name:str, brewery_type:str, address_1:str, address_2:str | None, address_3:str|None, city:str, state_province:str, postal_code:str, country:str, longitude:float|None, latitude:float|None, phone:str, website_url:str|None, state:str, street:str):
            self.id = id
            self.name = name
            self.brewery_type = brewery_type
            self.address_1 = address_1
            self.address_2 = address_2
            self.address_3 = address_3
            self.city = city
            self.state_province = state_province
            self.postal_code = postal_code
            self.country = country
            self.longitude = longitude
            self.latitude = latitude
            self.phone = phone
            self.website_url = website_url
            self.state = state
            self.street = street

        def __str__(self):
            return f"{self.name}, {self.brewery_type}, {self.city}, {self.street}"


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
        id = i["id"],
        name = i["name"],
        brewery_type= i["brewery_type"],
        address_1=i["address_1"],
        address_2=i["address_2"],
        address_3=i["address_3"],
        city = i["city"],
        state_province=i["state_province"],
        postal_code=i["postal_code"],
        country = i["country"],
        longitude=i["longitude"],
        latitude=i["latitude"],
        phone=i["phone"],
        website_url=i["website_url"],
        state=i["state"],
        street=i["street"]
    ))
for browar in lista:
    print(browar)
