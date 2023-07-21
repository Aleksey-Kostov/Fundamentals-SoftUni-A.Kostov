string = input()

command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        index, given_string = int(command[1]), command[2]
        if index in range(len(string)):
            string = string[:index] + given_string + string[index:]
        print(string)
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(string)) and end_index in range(len(string)):
            string = string[:start_index] + "" + string[end_index + 1:]
        print(string)
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
        print(string)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {string}")

