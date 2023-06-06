def closest_coordinates(coordinates: []):
    from math import floor
    sum_coordinates = []
    first_sum = 0
    second_sum = 0
    real_coord_one = 0
    real_coord_two = 0
    real_coord_four = 0
    real_coord_three = 0
    for digit in range(len(coordinates)):
        if digit == 0:
            first_sum += (abs(coordinates[digit]) - abs(coordinates[digit + 2])) + \
                         (abs(coordinates[digit + 1]) - abs(coordinates[digit + 3]))
            sum_coordinates.append(first_sum)
        elif digit == 4:
            second_sum += (abs(coordinates[digit]) - abs(coordinates[digit + 2])) + \
                          (abs(coordinates[digit + 1]) - abs(coordinates[digit + 3]))
            sum_coordinates.append(second_sum)
        if first_sum == max(sum_coordinates) and digit == 0:
            real_coord_one = coordinates[digit]
            real_coord_two = coordinates[digit + 1]
            real_coord_three = coordinates[digit + 2]
            real_coord_four = coordinates[digit + 3]
        elif second_sum == max(sum_coordinates) and digit == 4:
            real_coord_one = coordinates[digit]
            real_coord_two = coordinates[digit + 1]
            real_coord_three = coordinates[digit + 2]
            real_coord_four = coordinates[digit + 3]
    return f"{floor(real_coord_three), floor(real_coord_four)}" \
           f"{floor(real_coord_one), floor(real_coord_two)}"


first_coordinates = float(input())
second_coordinates = float(input())
third_coordinates = float(input())
fourth_coordinates = float(input())
fifth_coordinates = float(input())
sixth_coordinates = float(input())
seventh_coordinates = float(input())
eighth_coordinates = float(input())
list_coordinates = [first_coordinates, second_coordinates, third_coordinates, fourth_coordinates,
                    fifth_coordinates, sixth_coordinates, seventh_coordinates, eighth_coordinates]
print(closest_coordinates(list_coordinates))
