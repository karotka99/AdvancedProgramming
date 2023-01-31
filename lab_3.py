# ex1
def hello(name: str, surname: str) -> str:
    return 'Czesc ' + name + ' ' + surname + '!'


a = hello('Karolina', 'karotka99')
print(a)


# ex2
def mnozenie(x: int, y: int) -> int:
    return x * y


print(mnozenie(3, 4))


# ex3
def parzysta(b: int) -> bool:
    return b % 2 == 0


c = parzysta(5)

if c:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')


# ex4
def wieksza(d: int, e: int, f: int) -> bool:
    return d + e >= f


print(wieksza(1, 5, 8))


# ex5
def parametr(tab: list, g: int) -> bool:
    return g in tab


print(parametr([0, 8, 6, 5, 4, 3, 2], 3))


# ex6

def connect(tab1: list, tab2: list) -> list:
    new = set(tab1 + tab2)
    new1 = []
    for i in new:
        new1.append(i ** 3)
    return new1


print(connect([0, 1, 3, 5, 7], [4, 5, 6, 7]))
