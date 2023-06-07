def tribonacci_sequence(num: int):
    list_current_number = [1]
    sum_current_number = 0
    while list_current_number < list_current_number[num]:
        sum_current_number += 1
        if sum_current_number == current_number + current_number:
            list_current_number.append(current_number)
    return list_current_number


number = int(input())
print(*tribonacci_sequence(number), sep=" ")
