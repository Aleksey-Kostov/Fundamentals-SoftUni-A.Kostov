first_employee_efficiency_per_hour = int(input())
second_employee_efficiency_per_hour = int(input())
third_employee_efficiency_per_hour = int(input())
students_count = int(input())
hours_counter = 0
total_time = 0
total_efficiency_per_hour = first_employee_efficiency_per_hour + \
                            second_employee_efficiency_per_hour + \
                            third_employee_efficiency_per_hour
while students_count > 0:
    hours_counter += 1
    total_time += 1
    if hours_counter % 4 == 0:  # Break time
        continue
    students_count -= total_efficiency_per_hour
print(f"Time needed: {total_time}h.")
