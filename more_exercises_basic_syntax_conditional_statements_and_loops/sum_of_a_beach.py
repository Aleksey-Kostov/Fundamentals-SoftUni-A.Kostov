string = input()
word = ""
counter = 0

for char in string:
    word += char.lower()
    if "water" in word or "sand" in word or "fish" in word or "sun" in word:
        counter += 1
        word = ""
    else:
        continue

print(counter)
