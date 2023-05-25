separated_list = []
new_separated_list = []
string = input()
separated_list.append(string)
new_string = ""

for num in range(len(string)):
    current_string = string[num]
    if current_string == "-":
        new_string = string[num] + string[num + 1]
        new_string = abs(int(new_string))
        new_separated_list.append(new_string)
    elif current_string == " " or string[num - 1] == "-":
        continue
    elif num % 2 == 0:
        new_string = int(current_string)
        new_string *= -1
        new_separated_list.append(new_string)


print(new_separated_list)
