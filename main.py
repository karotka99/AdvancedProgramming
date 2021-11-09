class Produkt:
    def __init__(self, nazwa: str, numer_seryjny: int, numer_dostawcy: int, liczba_polproduktow: int, cena: float):
        self.nazwa = nazwa
        self.numer_seryjny = numer_seryjny
        self.numer_dostawcy = numer_dostawcy
        self.liczba_polproduktow = liczba_polproduktow
        self.cena = cena

    @property
    def __str__(self):
        return f"""Nazwa produktu: {self.nazwa},
        numer_seryjny: {self.numer_seryjny}
        numer_dostawcy: {self.numer_dostawcy},
        liczba_polproduktow: {self.liczba_polproduktow},
        cena: {self.cena}"""

class Magazyn:
    def __init__(self, produkt: str, numer_magazynu: int, ilosc_produktow: int, numer_telefonu: int, lokalizacja: str):
        self.produkt = produkt
        self.numer_magazynu = numer_magazynu
        self.ilosc_produktow = ilosc_produktow
        self.numer_telefonu = numer_telefonu
        self.lokalizacja = lokalizacja
    @property
    def __str__(self):
        return f"""Nazwa produktu: {self.produkt},
        numer_magazynu: {self.numer_magazynu}
        ilosc_produktow: {self.ilosc_produktow},
        numer_telefonu: {self.numer_telefonu},
        lokalizacja: {self.lokalizacja}"""

 class KlientDetaliczny:
      def __init__(self, imie: str, nazwisko: str, numer: int, adres: str, telefon: int):
         self.imie = imie
         self.nazwisko = nazwisko
         self.numer = numer
         self.adres = adres
         self.telefon = telefon

      @property
      def __str__(self):
        return f"""imie: {self.imie}, 
        nazwisko: {self.nazwisko}, 
        numer: {self.numer},
        adres: {self.adres}, 
        telefon: {self.telefon}"""

 class KlientBiznesowy:
     def __init__(self, imie: str, nazwisko: str, numer: int, adres: str, telefon: int):
         self.imie = imie
         self.nazwisko = nazwisko
         self.numer = numer
         self.adres = adres
         self.telefon = telefon

     @property
     def __str__(self):
        return f"""imie: {self.imie},
         nazwisko: {self.nazwisko}
         numer: {self.numer},
         adres: {self.adres},
         telefon: {self.telefon}"""

class Zamowienie:
    def __init__(self, numer_zamowienia : int, ilosc_produktow: int, klient: KlientDetaliczny, numer_magazynu: Magazyn, opis_produktu: Produkt):
        self.numer_zamowienia = numer_zamowienia
        self.ilosc_produktow = ilosc_produktow
        self.klient = klient
        self.numer_magazynu = numer_magazynu
        self.opis_produktu = opis_produktu

    def __str__(self):
        return f"""numer_zamowienia: {self.numer_zamowienia},
             ilosc_produktow: {self.ilosc_produktow}
             klient: {self.klient},
             numer_magazynu: {self.numer_magazynu},
             cena_produktu: {self.opis_produktu}"""

    @property
    def count(self) -> float:
      return round(self.ilosc_produktow * self.opis_produktu.cena,2)

    @property
    def adres(self) -> str:
        return self.klient.adres
'''
        @numer_zamowienia.setter
        def numer_zamowienia(self, value1):
            self._numer_zamowienia = value1

        @ilosc_produktow.setter
        def ilosc_produktow(self, value2):
            self._ilosc_produktow = value2

        @numer_magazynu.setter
        def numer_magazynu(self, value3):
            self._numer_magazynu = value3

        @ilosc_produktow.setter
        def ilosc_produktow(self, value4):
                self._ilosc_produktow = value4

        @klient.setter
        def klient(self, value5):
            self._klient = value5

        @opis_produktu.setter
        def opis_produktu(self, Produkt):
            self._opis_produktu = Produkt

'''


klient1=KlientDetaliczny('Karolina', 'Tatarczyk', 12345, 'Gliwice, ul.Akademicka 2a', 987654321)
magazyn1= Magazyn('dyski', 13 , 34456, 456456456, 'Katowice')
dysk= Produkt('dysk', 2343, 139, 1, 34.23)
zamowienie1=Zamowienie(12,34,klient1,magazyn1,dysk)
print(zamowienie1)






