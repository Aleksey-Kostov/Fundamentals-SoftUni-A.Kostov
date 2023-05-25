new_separated_list = []
string = input()
data_list = string.split(" ")

for num in range(len(data_list)):
    current_number = int(data_list[num])
    if current_number < 0:
        current_number = abs(current_number)
        new_separated_list.append(current_number)
    elif current_number > 0:
        current_number *= -1
        new_separated_list.append(current_number)
    else:
        new_separated_list.append(current_number)

print(new_separated_list)
