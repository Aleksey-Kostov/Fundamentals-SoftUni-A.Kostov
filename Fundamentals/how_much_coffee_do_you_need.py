events = input()
total_coffe = 0

events_lower = ["dog", "cat", "coding", "movie"]
events_upper = ["DOG", "CAT", "CODING", "MOVIE"]

while events != "END":
    if events in events_lower:
        total_coffe += 1
    elif events in events_upper:
        total_coffe += 2
    else:
        events = input()
        continue
    if total_coffe > 5:
        print("You need extra sleep")
        break
    events = input()

if total_coffe <= 5:
    print(total_coffe)
