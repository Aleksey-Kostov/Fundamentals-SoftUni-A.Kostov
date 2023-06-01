numbers = input().split()
new_numbers = []


def given_numbers():
    for number in numbers:
        new_numbers.append(round(float(number)))
    return new_numbers


print(given_numbers())
