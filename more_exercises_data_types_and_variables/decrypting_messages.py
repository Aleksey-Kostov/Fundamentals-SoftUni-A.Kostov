key = int(input())
number_of_line = int(input())
list_string = []


for number in range(number_of_line):
    character = input()
    new_string = key + ord(character)
    list_string.append(chr(new_string))

print("".join(list_string))
