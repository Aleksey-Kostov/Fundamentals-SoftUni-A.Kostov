number_of_snowballs = int(input())
current_value = []

current_snowball_weight = 0
current_snowball_time = 0
current_snowball_quality = 0
max_value = 0

for number in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality
    current_value.append(value)
    current_max_value = max(current_value)
    if max_value < current_max_value:
        max_value = current_max_value
        current_snowball_weight = snowball_weight
        current_snowball_time = snowball_time
        current_snowball_quality = snowball_quality

print(f"{current_snowball_weight} : {current_snowball_time} = "
      f"{max_value:.0f} ({current_snowball_quality})")
