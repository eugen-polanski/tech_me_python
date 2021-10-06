users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

dict_1 = users[0]
dict_2 = users[1]

print(templates[dict_1['age'] < 7].format(name = dict_1['name'], surname = dict_1['surname'], age = dict_1['age']))
print(templates[dict_2['age'] < 7].format(name = dict_2['name'], surname = dict_2['surname'], age = dict_2['age']))