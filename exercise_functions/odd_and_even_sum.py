
def make_sum_of_all_number():
    single_number = input()
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for digit in range(len(single_number)):
        if int(single_number[digit]) % 2 == 0:
            sum_of_even_digits += int(single_number[digit])
        else:
            sum_of_odd_digits += int(single_number[digit])
    print(f"Odd sum = {sum_of_odd_digits},", end=" ")
    print(f"Even sum = {sum_of_even_digits}")


make_sum_of_all_number()
