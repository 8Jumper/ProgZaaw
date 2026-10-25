class Browar:
    def __init__(self, id: str, name: str, brewery_type: str, address_1: str,
                 address_2: str | None, address_3: str | None, city: str,
                 state_province: str, postal_code: str, country: str,
                 longitude: float | None, latitude: float | None, phone: str,
                 website_url: str | None, state: str, street: str):
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
        return f"Name:{self.name}, Brewery type:{self.brewery_type},City: {self.city}, Street{self.street}"
