numbers = list(map(int, input().split()))
average_number = sum(numbers) // len(numbers)
new_list = []

for number in numbers:
    if number > average_number:
        new_list.append(number)
        new_list.sort(reverse=True)

if len(new_list) == 0:
    print("No")
else:
    print(*new_list[:5])
