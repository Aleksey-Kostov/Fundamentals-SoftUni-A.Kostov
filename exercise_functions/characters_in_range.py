def num_in_range(first_number, second_number):
    new_n = range(ord(first_number) + 1, ord(second_number))
    new_list = []
    for numbers in new_n:
        new_list.append(chr(numbers))
    return new_list


character_1 = input()
character_2 = input()
print(" ".join(num_in_range(character_1, character_2)))
