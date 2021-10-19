#ex2a
print()
print('Zadanie 2a:')
print()
def print_names(name_list):
    for i in range(len(name_list)):
        print(name_list[i])

names=['Karolina','Antoni','Joanna','Jan', 'Romek']
print_names(names)

print()
print('Zadanie 2b.1:')
print()
#ex2b.1
def numbers(numbers_list):
    for i in range(len(numbers_list)):
        numbers_list[i] *= 2
    return numbers_list


print(numbers([1,2,3,4,5]))

print()
print('Zadanie 2b.2:')
print()
#ex2b.2
def numbers2(numbers_list):
    return[2*i for i in numbers_list]

print(numbers2([1,2,3,4,5]))

print()
print('Zadanie 2c:')
print()
#ex2c
list=[1,45,46,78,980,23,45,23,2,80]
for i in range(len(list)):
    if list[i] % 2 == 0:
     print(list[i])


print()
print('Zadanie 2d:')
print()
#ex2d
list2=[1,45,46,78,980,23,45,23,2,80]
for i in range(len(list2)):
     if i % 2 == 1:
         print(list2[i])

