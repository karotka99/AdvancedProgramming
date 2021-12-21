from models.diet import Diet
from models.patient import Patient
from datetime import datetime


class Order:

    _order_id: int
    _date: datetime
    _diets: list[Diet]
    _client: Patient

    def __int__(self):
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

    def calculate_price(self) -> float:
        price = 0.0
        for r in self._diets:
            price += r.price
        return round(price, 2)

    def calculate_calories(self) -> float:
        total_calories = 0.0
        for k in self._diets:
            total_calories += k.calories
        return total_calories
