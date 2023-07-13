import re

pattern = r"(\d{2})([/.-])([A-Z][a-z]{2})\2(\d{4})"
date_text = input()
matches = re.findall(pattern, date_text)


for match in matches:
    date, separator, month, year = match
    print(f"Day: {date}, Month: {month}, Year: {year}")
