import re

multiple_digits = 1
current_digit = ""
emoji_list = []

text = input()
pattern = r"([*]{2}|[:]{2})([A-Z][a-z]{2,})\1"
matches = re.findall(pattern, text)

pattern_2 = r"\d+"
matches_digits = re.findall(pattern_2, text)

for digit in matches_digits:
    current_digit += digit

for digits in current_digit:
    multiple_digits *= int(digits)

for match in matches:
    emoji_list.append(match[0])
print(emoji_list)
print(multiple_digits)

