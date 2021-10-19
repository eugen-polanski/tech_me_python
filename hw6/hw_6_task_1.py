
some_list = [i for i in input('Введите числа: ').split()]
some_list2 = []

for i in range(len(some_list) - 1):
    if some_list[i] < some_list[i + 1]:
        some_list2.append(some_list[i + 1])

print(some_list2)
