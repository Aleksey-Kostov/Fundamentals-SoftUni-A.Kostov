days_of_the_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
current_plunder = 0

for day in range(1, days_of_the_plunder + 1):
    current_plunder += daily_plunder
    if day % 3 == 0:
        current_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        current_plunder *= 0.7


if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    percent = (current_plunder / expected_plunder) * 100
    print(f"Collected only {percent:.2f}% of the plunder.")
