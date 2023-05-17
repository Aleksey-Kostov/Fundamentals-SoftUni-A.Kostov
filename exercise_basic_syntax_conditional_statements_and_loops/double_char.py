characters = input()

while characters != "End":
    total_characters = ""
    if characters == "SoftUni":
        characters = input()
        continue
    for i in characters:
        total_characters += i * 2
    print(total_characters)
    characters = input()
    