centuries = int(input())

ONE_CENTURIES_YEARS = 100
ONE_CENTURIES_DAYS = 365.2422

centuries_years = centuries * ONE_CENTURIES_YEARS
centuries_days = centuries_years * ONE_CENTURIES_DAYS
centuries_hours = int(centuries_days) * 24
centuries_minutes = centuries_hours * 60

print(f"{centuries:.0f} centuries = {centuries_years:.0f} years ="
      f" {centuries_days:.0f} days = {centuries_hours:.0f} hours = {centuries_minutes:.0f} minutes")
