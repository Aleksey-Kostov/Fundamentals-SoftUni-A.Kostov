n = int(input())
special_number = [5, 7, 11]

for num in range(1, n + 1):
    number = 0
    flag = False
    for digits in (str(num)):
        number += int(digits)
    if number in special_number:
        flag = True
    if flag:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
