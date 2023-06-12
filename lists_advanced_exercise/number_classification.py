def separated_numbers(string_numbers):
    positive_numbers = [number for number in string_numbers if int(number) >= 0]
    negative_numbers = [number for number in string_numbers if int(number) < 0]
    even_numbers = [number for number in string_numbers if int(number) % 2 == 0]
    odd_numbers = [number for number in string_numbers if int(number) % 2 != 0]
    return positive_numbers, negative_numbers, even_numbers, odd_numbers


numbers = input().split(", ")
total_positive_numbers, total_negative_numbers, total_even_numbers, total_odd_numbers = separated_numbers(numbers)
print(f"Positive: {', '.join(total_positive_numbers)}")
print(f"Negative: {', '.join(total_negative_numbers)}")
print(f"Even: {', '.join(total_even_numbers)}")
print(f"Odd: {', '.join(total_odd_numbers)}")
