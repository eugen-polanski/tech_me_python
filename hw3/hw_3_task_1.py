user_data = input("Введите, пожалуйста, данные: \n >>> ")
list_data = user_data.split()

n = 0
l = len(list_data) - 1

while l > n:
    list_data[n], list_data[n + 1] = list_data[n + 1], list_data[n]
    n += 2

print(list_data)
