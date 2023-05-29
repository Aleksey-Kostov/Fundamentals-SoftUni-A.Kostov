string_numbers = input().split()
number_of_remove = int(input())
current_numbers = []

for num in range(len(string_numbers)):
    current_numbers.append(int(string_numbers[num]))

for numbers in range(number_of_remove):
    min_removed_numbers = min(current_numbers)
    current_numbers.remove(min_removed_numbers)

print(*current_numbers, sep=", ")
