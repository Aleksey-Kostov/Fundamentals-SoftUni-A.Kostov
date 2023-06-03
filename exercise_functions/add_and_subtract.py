def sum_numbers(num_1, num_2):
    result_sum = num_1 + num_2
    return result_sum


def subtract(sums, num_3):
    result = sums - num_3
    return result


def add_and_subtract(number1, number2, number3):
    sum_of_num_1_and_num_2 = sum_numbers(number1, number2)
    result = subtract(sum_of_num_1_and_num_2, number3)
    return result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(add_and_subtract(number_1, number_2, number_3))
