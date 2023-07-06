subtracts = input().split(chr(92))
file_and_extension = subtracts[-1].split(".")
extension = file_and_extension[0]
file = file_and_extension[1]

print(f"File name: {extension}")
print(f"File extension: {file}")
