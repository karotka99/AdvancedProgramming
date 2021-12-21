from models.diet import Diet


class Dietician:

    def __init__(self, name: str, surname: str,
                 diet_name: Diet, age: int):
        self._name = name
        self._surname = surname
        self._diet_name = diet_name
        self._age = age

    @property
    def product_name(self):
        return self._name

    @property
    def price(self):
        return self._surname

    @property
    def last_modified(self):
        return self._diet_name

    @property
    def description(self):
        return self._age

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
