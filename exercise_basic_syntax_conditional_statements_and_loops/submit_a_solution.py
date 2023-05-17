first_string = input()
second_string = input()
current_string = first_string

for characters in range(len(first_string)):
    left_part = second_string[:characters + 1]
    right_part = first_string[characters + 1:]
    full_string = left_part + right_part
    if current_string != full_string:
        print(full_string)
        current_string = full_string
