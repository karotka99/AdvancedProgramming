print('ex1')
print()

def hello(name:str, surname: str) -> str:
    return 'Czesc '+ name+ ' ' + surname + '!'

a=hello('Karolina','karotka99')
print(a)

print()
print('ex2')
print()
def mnozenie(x: int, y:int) -> int:
    return x*y

print(mnozenie(3,4))

print()
print('ex3')
print()

def parzysta(b: int) -> bool:
    return b%2 == 0

c=parzysta(5)

if(c==True):
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')



print()
print('ex4')
print()

def wieksza(d: int, e: int, f: int) -> bool:
     return d+e >=f


print(wieksza(1,5,8))

print()
print('ex5')
print()

def parametr(tab: list, g: int) -> bool:
    return g in tab

print(parametr([0,8,6,5,4,3,2],3))


print()
print('ex6')
print()

def connect(tab1: list, tab2: list) -> list:
    new=set(tab1+tab2)
    new1=[]
    for i in new:
        new1.append(i**3)
    return new1

print(connect([0,1,3,5,7],[4,5,6,7]))



