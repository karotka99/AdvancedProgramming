from models.diet import Diet
from models.patient import Patient
from datetime import datetime


class Order:

    _order_id: int
    _date: datetime
    _diets: list[Diet]
    _client: Patient

    def __init__(self):
        pass

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: int):
        self._order_id = order_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: datetime):
        self._date = date

    @property
    def diets(self):
        return self._diets

    @diets.setter
    def diets(self, diets: list[Diet]):
        self._diets = diets

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client: Patient):
        self._client = client

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def calculate_price(self):
        price = 0.0
        for elements in self._diets:
            price += elements.price
        return round(price, 2)

    def calculate_calories(self):
        total_calories = 0.0
        for element in self._diets:
            total_calories += element.calories
        return total_calories
