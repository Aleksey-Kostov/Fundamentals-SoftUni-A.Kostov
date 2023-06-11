def any_string_in(first_string_list, second_string_list):
    new_string_list = []
    for first_string in first_string_list:
        for second_string in second_string_list:
            if first_string in second_string:
                new_string_list.append(first_string)
                break
    return new_string_list


first_strings = input().split(', ')
second_strings = input().split(', ')
print(any_string_in(first_strings, second_strings))
