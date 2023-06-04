def min_max_and_sum_numbers(num: []) -> {}:
    number_integer = []
    for number in num:
        number_integer.append(int(number))
    max_number = max(number_integer)
    min_number = min(number_integer)
    sum_number = sum(number_integer)
    return max_number, min_number, sum_number


integer_numbers = input().split()
max_num, min_num, sum_num = min_max_and_sum_numbers(integer_numbers)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")
