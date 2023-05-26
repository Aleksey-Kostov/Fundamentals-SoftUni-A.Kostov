card = input()
card_collect = card.split(" ")
card_collect_filtered = set(card_collect)
new_card_collect_filtered = []
team_a = 11
team_b = 11

for index, digit in enumerate(card_collect_filtered):
    new_card_collect_filtered.append(digit)
    if "A" in new_card_collect_filtered[index]:
        team_a -= 1
    elif "B" in new_card_collect_filtered[index]:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break

print(f"Team A - {team_a};", end=" " f"Team B - {team_b}")
if team_a < 7 or team_b < 7:
    print(f"\nGame was terminated")
