centuries = int(input())

ONE_CENTURIES_YEARS = 100
ONE_CENTURIES_DAYS = 365.2422

centuries_years = centuries * ONE_CENTURIES_YEARS
centuries_days = centuries_years * ONE_CENTURIES_DAYS
centuries_hours = int(centuries_days) * 24
centuries_minutes = int(centuries_hours) * 60

print(f"{centuries} centuries = {centuries_years} years ="
      f" {int(centuries_days)} days = {centuries_hours} hours = {centuries_minutes} minutes")
