year = int(input())

while True:
    year += 1
    string_next_year = str(year)
    set_value = set(string_next_year)
    if len(set_value) == len(string_next_year):
        break

print(year)
