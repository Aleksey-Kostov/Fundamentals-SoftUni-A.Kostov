def fill_elektron(number_elektron, list_elektron):
    list_numbers = []
    numbers = 0
    for number in list_elektron:
        if number + sum(list_numbers) < number_elektron:
            list_numbers.append(number)
            numbers += number
        elif number + sum(list_numbers) > number_elektron and sum(list_numbers) - number_elektron != 0:
            list_numbers.append(number_elektron - numbers)
            break
    return list_numbers


elektron = int(input())
number_of_elektron = [2 * number ** 2 for number in range(1, elektron + 1)]
total_elektron = fill_elektron(elektron, number_of_elektron)
print(total_elektron)
