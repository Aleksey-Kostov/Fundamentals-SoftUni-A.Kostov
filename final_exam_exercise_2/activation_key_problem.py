activation_key = input()

new_digit_low = ""
new_digit_up = ""
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
                new_digit_low += digit_low.lower()
            for_replace = activation_key[start_index:end_index]
            activation_key = activation_key.replace(for_replace, new_digit_low)
            print(activation_key)
        elif command[1] == "Upper":
            for digit_up in activation_key[start_index:end_index]:
                new_digit_up += digit_up.upper()
            for_replace_up = activation_key[start_index:end_index]
            activation_key = activation_key.replace(for_replace_up, new_digit_up)
            print(activation_key)
    elif command[0] == "Slice":
        slice_start_index = int(command[1])
        slice_end_index = int(command[2])
        slice_for_replace = activation_key[slice_start_index:slice_end_index]
        activation_key = activation_key.replace(slice_for_replace, "")
        print(activation_key)
    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")
