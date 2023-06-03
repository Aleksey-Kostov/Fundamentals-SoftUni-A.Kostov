
def make_sum_of_all_number(current_number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for digit in range(len(current_number)):
        if int(current_number[digit]) % 2 == 0:
            sum_of_even_digits += int(current_number[digit])
        else:
            sum_of_odd_digits += int(current_number[digit])
    return sum_of_odd_digits, sum_of_even_digits


single_number = input()
odd_digits, even_digits = make_sum_of_all_number(single_number)
print(f"Odd sum = {odd_digits},", end=" ")
print(f"Even sum = {even_digits}")
