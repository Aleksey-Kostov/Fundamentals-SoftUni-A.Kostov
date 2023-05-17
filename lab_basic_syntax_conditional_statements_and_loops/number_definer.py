point_number = float(input())

if point_number == 0:
    print("zero")
elif point_number > 0:
    if 0 < point_number < 1:
        print("small positive")
    elif point_number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if 0 < abs(point_number) < 1:
        print("small negative")
    elif abs(point_number) > 1000000:
        print("large negative")
    else:
        print("negative")
