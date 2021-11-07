class Property:
    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"""
        Area: {self.area}
        Rooms: {self.rooms}
        Price: {self.price}
        Address: {self.address} 
            """


class House(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"""
        Area: {self.area}
        Rooms: {self.rooms}
        Price: {self.price}
        Address: {self.address} 
        Plot: {self.plot}
        """


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"""
        Area: {self.area}
        Rooms: {self.rooms}
        Price: {self.price}
        Address: {self.address} 
        Floor: {self.floor}
        """


House_1 = House('150 m2', 5, 814210, 'Wodzisław Śląski Szkolna 29', 1)
Flat_1 = Flat('40 m2', 4, 140821, 'Jastrzębie Zdrój Wyzwolenia 13', 2)
print(House_1)
print(Flat_1)
