single_string = [int(string)for string in input().split(", ")]
for digit in single_string:
    if digit == 0:
        single_string.remove(digit)
        single_string.append(digit)

print(single_string)
