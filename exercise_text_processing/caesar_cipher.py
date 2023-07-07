text = input()
ascii_char = ""

for char in text:
    number_char = ord(char)
    ascii_char += chr(number_char + 3)

print(ascii_char)
