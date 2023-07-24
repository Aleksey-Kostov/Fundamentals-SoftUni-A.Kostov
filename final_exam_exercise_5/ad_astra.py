import re
text_string = input()
calories_list = []

pattern = r"([|#]{1})([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.findall(pattern, text_string)

for match in matches:
    calories_list.append(int(match[3]))

total_calories = sum(calories_list)
needed_days = total_calories // 2000

print(f"You have food to last you for: {needed_days} days!")
for item in matches:
    print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")
