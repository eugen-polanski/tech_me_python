month_number = input("Введите, пожалуйста, номер месяца: \n>>> ")

seasons = ['',
           'Зима', 'Зима', 'Весна', 'Весна',
           'Весна', 'Лето', 'Лето', 'Лето',
           'Осень', 'Осень', 'Осень','Зима']

if month_number.isdigit() and int(month_number) in range(1, 13):
    result = seasons[int(month_number)]
else:
    result = "Введите, пожалуйста, корректный номер месяца"

print(result)