import re

participants_dict = {}
new_dict = {}
list_of_participants = input().split(", ")
for participants in list_of_participants:
    participants_dict[participants] = 0

sum_distance = 0
name_participants = ""
string = input()
while string != "end of race":
    pattern = r"\w"
    matches = re.findall(pattern, string)
    for match in matches:
        if match.isdigit():
            sum_distance += int(match)
        elif match.isalpha():
            name_participants += match
    if name_participants in participants_dict:
        participants_dict[name_participants] += sum_distance
        new_dict = \
            {k: v for k, v in sorted(participants_dict.items(), key=lambda item: -item[1])}
    sum_distance = 0
    name_participants = ""
    string = input()

counter = 0
for key in new_dict.keys():
    counter += 1
    if counter == 1:
        print(f"1st place: {key}")
    elif counter == 2:
        print(f"2nd place: {key}")
    elif counter == 3:
        print(f"3rd place: {key}")
    elif counter > 3:
        break
