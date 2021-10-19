def user_data(name, surname, patronymic, birth_year, city, email, phone_number):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    birth_year = int(input('Введите год рождения: '))
    city = input('Введите город проживания: ')
    email = input('Введите e-mail: ')
    phone_number = int(input('Введите телфонный номер: '))
    print(f'{surname} {name} {patronymic} {birth_year}'
          f' года рождения, проживающий в городе {city}.'
          f' \n Контактные данные:\n- {email}\n- {phone_number}'
          )


user_data('name', 'surname', 'patronymic', 'birth_year', 'city', 'email', 'phone_number')
