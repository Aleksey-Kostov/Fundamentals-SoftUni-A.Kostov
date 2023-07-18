import re

number_of_barcode = int(input())

pattern = "((@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,}))"
barcode_list = []
new_barcode_list = []
code_for_product = ""

for code in range(number_of_barcode):
    barcode = input()
    matches = re.findall(pattern, barcode)
    barcode_list.append(matches)

for code in barcode_list:
    if code:
        for j in code:
            new_barcode_list.append(j[0])
    else:
        new_barcode_list.append("0")

for barcode in new_barcode_list:
    if barcode != "0":
        for digits in range(len(barcode)):
            if barcode[digits].isdigit():
                code_for_product += barcode[digits]
    else:
        print("Invalid barcode")
        continue
    if code_for_product != "":
        print(f"Product group: {code_for_product}")
    else:
        print("Product group: 00")
    code_for_product = ""
