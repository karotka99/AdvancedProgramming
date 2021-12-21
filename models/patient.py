class Patient:

    def __init__(self, name: str, surname: str,
                 weight: float, age: int):
        self._name = name
        self._surname = surname
        self._age = age
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
