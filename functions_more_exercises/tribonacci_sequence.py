def tribonacci_sequence(num: int):
    list_current_number = [1]
    sum_current_number = 0
    while True:
        sum_current_number += 1
        list_current_number.pop(0)
        if sum_current_number == sum(list_current_number):
            list_current_number.append(sum_current_number)
        if len(list_current_number) == num:
            break
    return list_current_number


number = int(input())
print(*tribonacci_sequence(number), sep=" ")
