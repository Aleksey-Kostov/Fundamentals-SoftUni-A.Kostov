factor_number = int(input())
count_number = int(input())

multiplier = factor_number * count_number
list_numbers = []

for number in range(factor_number, multiplier + 1):
    if number % factor_number == 0:
        list_numbers.append(number)

print(list_numbers)
