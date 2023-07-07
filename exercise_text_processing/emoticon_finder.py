text = input()
emoticons = ""
list_emoticons = []

for char in range(len(text)):
    if text[char] == ":":
        emoticons = text[char] + text[char + 1]
        list_emoticons.append(emoticons)

print("\n".join(list_emoticons))

