list_of_characters = input().split(", ")
characters_dict = {character: ord(character) for character in list_of_characters}
print(characters_dict)
