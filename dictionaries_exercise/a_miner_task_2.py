string = input()
resource_dict = {}
resource_list = []

while string != "stop":
    resource_list.append(string)
    string = input()

for i in range(0, len(resource_list), 2):
    key = resource_list[i]
    value = int(resource_list[i + 1])
    if key not in resource_dict.keys():
        resource_dict[key] = 0
    resource_dict[key] += value

for resource, quantity in resource_dict.items():
    print(f"{resource} -> {quantity}")
