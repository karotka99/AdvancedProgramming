
class Diet:

    def __init__(self, diet_name: str, price: float,
                 lasting_days: int, calories: float):
        self._diet_name = diet_name
        self._price = price
        self._lasting_days = lasting_days
        self._calories = calories

    @property
    def product_name(self):
        return self._diet_name

    @property
    def price(self):
        return self._price

    @property
    def last_modified(self):
        return self._lasting_days

    @property
    def calories(self):
        return self._calories

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
