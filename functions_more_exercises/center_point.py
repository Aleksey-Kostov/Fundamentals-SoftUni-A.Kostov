def closest_coordinates(coordinates):
    from math import floor
    sum_coordinates = []
    twice_sum = 0
    real_coord_one = 0
    real_coord_two = 0
    for digit in range(len(coordinates)):
        if digit % 2 == 0:
            twice_sum = abs(coordinates[digit]) + abs(coordinates[digit + 1])
            sum_coordinates.append(twice_sum)
        elif digit != 0:
            continue
        if twice_sum == min(sum_coordinates):
            real_coord_one = coordinates[digit]
            real_coord_two = coordinates[digit + 1]
    return floor(real_coord_one), floor(real_coord_two)


first_coordinates = float(input())
second_coordinates = float(input())
third_coordinates = float(input())
fourth_coordinates = float(input())
list_coordinates = [first_coordinates, second_coordinates, third_coordinates, fourth_coordinates]
print(closest_coordinates(list_coordinates))
