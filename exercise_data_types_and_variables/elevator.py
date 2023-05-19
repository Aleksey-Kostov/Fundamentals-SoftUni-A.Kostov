from math import ceil

number_of_persons = int(input())
capacity_of_elevator = int(input())

courses_elevator = number_of_persons / capacity_of_elevator

print(ceil(courses_elevator))
