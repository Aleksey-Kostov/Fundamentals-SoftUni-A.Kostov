def num_in_range(new_number):
    new_list = []
    result = ""
    for numbers in new_number:
        result += chr(numbers) + " "
        new_list = [result]
    return new_list


character_1 = input()
character_2 = input()
new_n = range(ord(character_1) + 1, ord(character_2))
print(*num_in_range(new_n))
