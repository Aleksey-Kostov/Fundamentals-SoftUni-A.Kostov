list_of_elements = list(map(int, input().split()))
command = input()

while command != "end":
    command_list = list(command.split())
    if command_list[0] == "swap":
        list_of_elements[int(command_list[1])], list_of_elements[int(command_list[2])] =\
            list_of_elements[int(command_list[2])], list_of_elements[int(command_list[1])]
    elif command_list[0] == "multiply":
        list_of_elements[int(command_list[1])] *= list_of_elements[int(command_list[2])]
    elif command_list[0] == "decrease":
        list_of_elements = list(map(lambda x: x - 1, list_of_elements))
    command = input()

print(*list_of_elements, sep=", ")
