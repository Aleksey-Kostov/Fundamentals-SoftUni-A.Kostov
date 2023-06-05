def is_number_perfect(num):
    is_perfect = False
    range_perfect_num = range(1, num)
    perfect_num = 0
    for numbers in range_perfect_num:
        if num % numbers == 0:
            perfect_num += numbers
    if perfect_num == num:
        is_perfect = True
    return is_perfect


number = int(input())
is_perfect_number = is_number_perfect(number)
if is_perfect_number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
