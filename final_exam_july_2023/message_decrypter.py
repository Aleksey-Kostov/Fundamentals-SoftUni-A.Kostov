import re

number_of_message = int(input())

for match in range(number_of_message):
    message = input()
    pattern = r"(^[$%])([A-Z][a-z]{3,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
    matches = re.findall(pattern, message)
    if not matches:
        print("Valid message not found!")
    else:
        for current_match in matches:
            descript_message = ((chr(int(current_match[2]))) +
                                (chr(int(current_match[3]))) +
                                (chr(int(current_match[4]))))
            print(f"{current_match[1]}: {descript_message}")
