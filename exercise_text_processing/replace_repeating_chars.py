string = input()
letter_list = []
current_char = ""

for char in range(len(string)):
    if current_char != string[char]:
        letter_list.append(string[char])
    current_char = string[char]


print(*letter_list, sep="")
