single_number = int(input())

filter_category = []
list_number = []

for i in range(single_number):
    current_number = int(input())
    list_number.append(current_number)

command = input()

if command == "even":
    for number in list_number:
        if number % 2 == 0:
            filter_category.append(number)
elif command == "odd":
    for number in list_number:
        if number % 2 != 0:
            filter_category.append(number)
elif command == "negative":
    for number in list_number:
        if number < 0:
            filter_category.append(number)
elif command == "positive":
    for number in list_number:
        if number >= 0:
            filter_category.append(number)

print(filter_category)
