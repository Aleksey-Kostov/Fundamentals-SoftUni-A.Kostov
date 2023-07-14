import re

text = input()
pattern = r"\b(_)([a-zA-Z0-9]+)\b"
matches = re.findall(pattern, text)
new_matches = []

for match in matches:
    for j in match:
        if j != "_":
            new_matches.append(j)

print(",".join(new_matches))
