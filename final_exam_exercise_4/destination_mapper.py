import re

string = input()
destination_list = []
travel_points = 0

pattern = r"([=|\/]{1})([A-Z][A-Za-z]{2,})\1"
result = re.finditer(pattern, string)

for destination in result:
    destination_list.append(destination.group(2))

for destinations in destination_list:
    travel_points += len(destinations)

print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {travel_points}")
