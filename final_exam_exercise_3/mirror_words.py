import re
mirror_list = []
matches = []

text = input()
pattern = r"(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
result = re.finditer(pattern, text)

for world in result:
    substring_1 = world.group(2)
    substring_2 = world.group(3)
    matches.append(world.group())
    if substring_1 == substring_2[::-1]:
        new_string = substring_1 + " <=> " + substring_2
        mirror_list.append(new_string)

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_list:
    print(f"The mirror words are:\n{', '.join(mirror_list)}")
else:
    print("No mirror words!")
