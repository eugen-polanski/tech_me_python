
some_list = [int(i) for i in input('Введите числа: ').split()]
some_list2 = []

for i in some_list:
    if some_list.count(i) == 1:
        some_list2.append(i)

print(some_list2)
