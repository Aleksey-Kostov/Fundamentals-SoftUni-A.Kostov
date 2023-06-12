def fill_elektron(number_elektron, list_elektron):
    numbers = 0
    for number in list_elektron:
        if numbers < number_elektron:
            numbers += number
        else:
            numbers += number_elektron - numbers
            break



elektron = int(input())
number_of_elektron = [2 * number ** 2 for number in range(1, elektron + 1)]
print(number_of_elektron)
total_elektron = list(filter(fill_elektron(elektron, number_of_elektron), number_of_elektron))
print(total_elektron)
