import re

count_of_barcode = int(input())

for bar in range(count_of_barcode):
    barcode = input()
    pattern = r"(@{1}#{1,})([A-Z][A-Za-z\d]{4,}[A-Z])(\@{1}#{1,})"
    matches = re.findall(pattern, barcode)
    if not matches:
        print("Invalid barcode")
    else:
        for match in matches:
            group_barcode = match[1]
            digit_in_barcode = [digit for digit in group_barcode if digit.isdigit()]
            new_barcode = "".join(digit_in_barcode)
            if new_barcode:
                print(f"Product group: {new_barcode}")
            else:
                print("Product group: 00")
