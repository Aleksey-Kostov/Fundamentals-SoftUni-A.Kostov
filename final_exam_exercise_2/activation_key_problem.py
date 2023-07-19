activation_key = input()

command = input().split(">>>")
while command[0] != "Generate":
    if command[0] == "Contains":
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Lower":
            for digit_low in activation_key[start_index:end_index]:
                new_digit = digit_low.casefold()
            print(activation_key)
        elif command[1] == "Upper":
            for digit_up in activation_key[start_index:end_index]:
                activation_key.replace(digit_up, digit_up.upper())
            print(activation_key)
    elif command[0] == "Slice":
        pass

    command = input().split(">>>")
