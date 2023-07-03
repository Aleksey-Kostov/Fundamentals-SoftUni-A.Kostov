text_characters = [character for character in input() if character != " "]
characters_dict = {}

for character in text_characters:
    if character not in characters_dict.keys():
        characters_dict[character] = 0
    characters_dict[character] += 1

for key, value in characters_dict.items():
    print(f"{key} -> {value}")
