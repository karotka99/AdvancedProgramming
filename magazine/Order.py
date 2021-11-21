import magazine.utils as Util


class Order:

    def __init__(self, client):
        self._client = client

    def __str__(self) -> str:
        return f"{self._client} and {Util.util_test(self._client)}"
