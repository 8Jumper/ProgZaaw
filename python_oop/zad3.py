
class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, plot: int, area, rooms: int, price, address):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom:\n"
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m2\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price} zl\n"
            f"Powierzchnia działki: {self.plot} m2"
        )


class Flat(Property):
    def __init__(self, floor, area, rooms: int, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie:\n"
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m2\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price} zl\n"
            f"Piętro: {self.floor}"
        )


# Tworzenie obiektów
house = House(500, 150, 5, 850000, "ul. Leśna 10")
flat = Flat(3, 60, 3, 450000, "ul. Kwiatowa 5")

# Wyświetlanie obiektów
print(house)
print()
print(flat)
