number = int(input())
is_prime = False
list_numbers = []

for num in range(1, number + 1):
    for i in range(1, num + 1):
        result = num * i
        if result == number:
            list_numbers.append(result)

if len(list_numbers) > 1:
    print(is_prime)
else:
    is_prime = True
    print(is_prime)
