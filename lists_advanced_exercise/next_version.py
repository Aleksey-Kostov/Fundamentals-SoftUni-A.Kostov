string = input().split(".")
new_digit = ""
for digit in string:
    new_digit += digit
integer_new_version = int(new_digit) + 1
print(".".join(str(integer_new_version)))
