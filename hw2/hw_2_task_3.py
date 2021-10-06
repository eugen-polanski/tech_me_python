numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

len(numbers)

compare_numbers = [numbers[0] % 2, numbers[1] % 2, numbers[2] % 2, numbers[3] % 2, numbers[4] % 2,
                   numbers[5] % 2, numbers[6] % 2, numbers[7] % 2, numbers[8] % 2, numbers[9] % 2, numbers[10] % 2]

even.append(numbers[0]), even.append(numbers[1]), even.append(numbers[2]), even.append(numbers[5]),
even.append(numbers[6]), even.append(numbers[7]), even.append(numbers[9])

odd.append(numbers[3]), odd.append(numbers[4]),
odd.append(numbers[8]), odd.append(numbers[10])

print(even)
print(odd)