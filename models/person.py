class Person:

    def __init__(self, firstname: str, lastname: str, age: int):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    @property
    def age(self) -> str:
        return self._age

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()