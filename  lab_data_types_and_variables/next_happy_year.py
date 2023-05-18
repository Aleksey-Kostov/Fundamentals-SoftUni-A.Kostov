happy_new_year = int(input())
new_years = happy_new_year + 1
next_happy_new_year = ""

while True:
    string_next_years = str(new_years)
    for i in range(len(string_next_years)):
        if string_next_years[i] not in next_happy_new_year:
            next_happy_new_year += string_next_years[i]
    if len(next_happy_new_year) == len(string_next_years):
        break
    new_years += 1
    next_happy_new_year = ""

print(next_happy_new_year)
