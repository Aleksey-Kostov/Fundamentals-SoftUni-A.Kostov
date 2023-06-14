numbers = list(map(int, input().split()))
counter = [numbers.count(num) for num in numbers]
counter = sum(counter)
average_number = sum(numbers) / counter
new_list = []

for number in range(len(numbers)):
    if numbers[-1] > average_number != sum(numbers):
        new_list.append(numbers)
        if new_list.count(numbers) == 5:
            print(*new_list)
            break
    if average_number == sum(numbers):
        print("No")
    print(*new_list)


