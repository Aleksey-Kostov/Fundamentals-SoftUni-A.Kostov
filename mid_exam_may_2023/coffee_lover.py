starting_list = input().split()
number_of_commands = int(input())
index = 0

for command in range(number_of_commands):
    commands = input()
    commands_list = commands.split()
    if commands_list[0] == "Include":
        starting_list.append(commands_list[1])
    elif commands_list[0] == "Remove":
        index = int(commands_list[2])
        if commands_list[1] == "first" and index in range(len(starting_list)):
            for coffe in starting_list[:index]:
                starting_list.remove(coffe)
        elif commands_list[1] == "last" and index in range(len(starting_list)):
            for coffe in starting_list[-index:]:
                starting_list.remove(coffe)
    elif commands_list[0] == "Prefer":
        index_coffe_1 = int(commands_list[1])
        index_coffe_2 = int(commands_list[2])
        if index_coffe_1 in range(len(starting_list)) and index_coffe_2 in range(len(starting_list)):
            starting_list[index_coffe_1], starting_list[index_coffe_2] =\
                starting_list[index_coffe_2], starting_list[index_coffe_1]
    elif commands_list[0] == "Reverse":
        starting_list.reverse()

print("Coffees:")
print(" ".join(starting_list))
