def sum_numbers(num_1, num_2):
    result_sum = num_1 + num_2
    return result_sum


def subtract(num_1, num_2, num_3):
    result = sum_numbers(num_1, num_2) - num_3
    return result


def add_and_subtract():
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())
    return subtract(number_1, number_2, number_3)


print(add_and_subtract())
