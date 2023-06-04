def validator_palindrome(some_numbers):
    if some_numbers == some_numbers[::-1]:
        return True
    return False


positive_integers = input().split(", ")
for number in positive_integers:
    print(validator_palindrome(number))
