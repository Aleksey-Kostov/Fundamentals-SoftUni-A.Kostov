import re
new_text = ""

while True:
    text = input()
    if text:
        new_text += " " + text
    else:
        break
pattern = r"\d+"
matches = re.findall(pattern, new_text)

print(" ".join(matches))
