data_list = input().split()
command = input()


def command_merge(current_list, command_1, command_2):
    new_characters = ""
    for characters in current_list[int(command_1)]:
        new_characters += characters
        for char in range(int(command_2)):
            current_list.append(new_characters)
    return current_list


def command_divide(current_list):
    pass
    return current_list


while command != "3:1":
    current_command = command.split()
    if current_command[0] == "merge":
        command_merge(data_list, current_command[1], current_command[2])
    elif current_command[0] == "divide":
        pass


print(" ".join(data_list))
