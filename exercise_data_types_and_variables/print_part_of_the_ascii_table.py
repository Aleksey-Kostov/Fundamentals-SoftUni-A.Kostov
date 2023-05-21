first_index_character = int(input())
second_index_character = int(input())
characters = ""

for index in range(first_index_character, second_index_character + 1):
    characters += chr(index) + " "

print(characters)
