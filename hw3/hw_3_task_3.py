user_data = input("Введите, пожалуйста, слова через пробел: \n >>> ")
list_data = user_data.split(' ')

n = 0
while n < len(list_data):
    if len(list_data[n]) <= 10:
        print(f"{n + 1}: {list_data[n].center(10,' ')} \n")
    else:
        print(f"{n + 1}: {list_data[n][:10]} \n")
    n += 1