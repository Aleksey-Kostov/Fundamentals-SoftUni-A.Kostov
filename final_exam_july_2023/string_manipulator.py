string = input()

command = input().split()

while command[0] != "End":
    action = command[0]
    if action == "Translate":
        character = command[1]
        replacement = command[2]
        string = string.replace(character, replacement)
        print(string)
    elif action == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif action == "Start":
        subs = command[1]
        if string.startswith(subs):
            print("True")
        else:
            print("False")
    elif action == "Lowercase":
        string = string.lower()
        print(string)
    elif action == "FindIndex":
        char = command[1]
        index_char = 0
        # index = string[::-1].index(char)   # variant 2
        # new_index = (len(string) - 1) - index   # variant 2

        for i in range(len(string)):
            if string[i] == char:
                current_index_char = i
                if current_index_char > index_char:
                    index_char = current_index_char
        print(index_char)
        # print(new_index)   # variant 2
    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        end_index = start_index + count
        string = string[:start_index] + string[end_index:]
        print(string)
    command = input().split()
