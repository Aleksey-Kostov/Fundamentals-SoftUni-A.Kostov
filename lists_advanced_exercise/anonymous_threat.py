data_list = input().split()
command = input()


def command_merge(current_list, command_1, command_2):
    new_characters = ""
    if int(command_1) in range(len(current_list)) and int(command_2) in range(len(current_list)):
        for characters in current_list[int(command_1):int(command_2) + 1]:
            new_characters += characters
            current_list.remove(characters)
    elif int(command_1) in range(len(current_list)):
        for characters in current_list[int(command_1):]:
            new_characters += characters
            current_list.remove(characters)
    elif int(command_2) in range(len(current_list)):
        for characters in current_list[int(command_2):]:
            new_characters += characters
            current_list.remove(characters)
    current_list.insert(int(command_1), new_characters)
    return current_list


def command_divide(current_list, command_1, command_2):
    from math import ceil
    current_characters = ""
    current_counter = 0
    total_counter = 0
    for characters in current_list[int(command_1):int(command_2) + 1]:
        for index, digits in enumerate(characters):
            if len(characters) % int(command_2) == 0:
                counter = len(characters) / int(command_2)
                if current_counter != counter:
                    current_characters += digits
                    current_counter += 1
                if current_counter == counter:
                    current_characters += " "
                    current_counter = 0
            else:
                counter = len(characters) // int(command_2)
                if current_counter != counter or counter == 0:
                    current_characters += digits
                    current_counter += 1
                elif current_counter == counter:
                    if total_counter != ceil(counter):
                        current_characters += " "
                        current_counter = 0
                        total_counter += 1
                    elif total_counter == ceil(counter):
                        current_characters += digits
        current_list.remove(characters)
        current_list.append(current_characters)
    return current_list


while command != "3:1":
    current_command = command.split()
    if current_command[0] == "merge":
        command_merge(data_list, current_command[1], current_command[2])
    elif current_command[0] == "divide":
        command_divide(data_list, current_command[1], current_command[2])
    command = input()


print(" ".join(data_list))
