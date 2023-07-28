def take_odd(current_string):
    string_for_action = ""
    for index in range(len(current_string)):
        if index % 2 != 0:
            string_for_action += current_string[index]
    return string_for_action


def cut(current_string, current_command):
    index = int(current_command[1])
    length = int(current_command[2])
    start_index = index
    end_index = index + length
    current_string = current_string[:start_index] + current_string[end_index:]
    return current_string


def substitute(current_string, current_command):
    substring = current_command[1]
    current_substitute = current_command[2]
    if substring not in current_string:
        print("Nothing to replace!")
    else:
        current_string = current_string.replace(substring, current_substitute)
        print(current_string)
    return current_string


string = input()

command = input().split()

while command[0] != "Done":
    action = command[0]
    if action == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif action == "Cut":
        string = cut(string, command)
        print(string)
    elif action == "Substitute":
        string = substitute(string, command)
    command = input().split()

print(f"Your password is: {string}")
