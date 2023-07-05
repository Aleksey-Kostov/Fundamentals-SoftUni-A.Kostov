string = input().split()
result = ""
for world in string:
    length = len(world)
    result += world * length

print(result)
