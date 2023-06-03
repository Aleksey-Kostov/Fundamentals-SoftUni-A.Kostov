character_1 = input()
character_2 = input()
n = range(ord(character_1) + 1, ord(character_2))
new_n = []


def num_in_range(a, b):
    for num in n:
        new_n.append(num)

    for numbers in new_n:
        result = (chr(numbers))
        print(result, end=" ")


num_in_range(character_1, character_2)