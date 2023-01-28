# ex2a
def print_names(name_list):
    for name in name_list:
        print(name)


names = ['Karolina', 'Antoni', 'Joanna', 'Jan', 'Romek']
print_names(names)


# ex2b.1


def numbers(numbers_list):
    for el in range(len(numbers_list)):
        numbers_list[el] *= 2
    return numbers_list


print(numbers([1, 2, 3, 4, 5]))


# ex2b.2


def numbers2(numbers_list):
    return [2 * elements for elements in numbers_list]


print(numbers2([1, 2, 3, 4, 5]))

# ex2c
lista_liczb = [1, 45, 46, 78, 980, 23, 45, 23, 2, 80]
for element in lista_liczb:
    if element % 2 == 0:
        print(element)

# ex2d
list2 = [1, 45, 46, 78, 980, 23, 45, 23, 2, 80]
for i in range(len(list2)):
    if i % 2 == 1:
        print(list2[i])
