numbers_of_line = int(input())
list_brackets_one = []
full_list = []
is_balanced = False

for num in range(numbers_of_line):
    string = input()
    if string == "(" or string == ")":
        full_list.append(string)

for digit in range(0, len(full_list), 2):
    if digit + 1 in range(len(full_list)):
        if full_list[digit] != full_list[digit + 1]:
            is_balanced = True
        else:
            is_balanced = False
            break
    else:
        if digit % 2 == 0:
            is_balanced = False
        else:
            is_balanced = is_balanced


if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
