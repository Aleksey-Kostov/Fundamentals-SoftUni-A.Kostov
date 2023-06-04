def sorted_numbers(numbers):
    int_number = []
    for number in numbers:
        int_number.append(int(number))
    numbers = sorted(int_number)
    return numbers


numbers_integer = input().split()
print(sorted_numbers(numbers_integer))
