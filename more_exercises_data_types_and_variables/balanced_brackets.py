numbers_of_line = int(input())
list_brackets_one = []
full_list = []
is_balanced = True
last_string = ""


for num in range(numbers_of_line):
    string = input()
    full_list.append(string)
for strings in range(len(full_list)):
    if len(full_list) == 1:
        is_balanced = True
        break
    elif full_list[-1] == "" and full_list[-2] == ")" or full_list[-1] == "(" or full_list[0] == "" \
            and full_list[1] == ")" or full_list[0] == ")" or full_list.count("(") != full_list.count(")") or\
            full_list[-2] == "(" and full_list[-1] == "":
        is_balanced = False
        break
    elif full_list[strings] == "(" and full_list[strings + 1:] == "(" or full_list[strings] == ")" and\
            full_list[strings + 1:] == ")":
        is_balanced = False
        break
    else:
        is_balanced = True


if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
