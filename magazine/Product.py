import magazine.utils as util


class Product:

    def __init__(self, name):
        self._name = name

    def __str__(self) -> str:
        return f"Product {self._name} and {util.util_test(self._name)}"
