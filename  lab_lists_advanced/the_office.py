def employees_happiness(list_employee, factor):
    sorted_happiness_list = []
    integer_list_employ = []
    for employee in list_employee:
        happiness = int(employee) * factor
        integer_list_employ.append(happiness)
    average_happiness = sum(integer_list_employ) / len(integer_list_employ)
    for employ in integer_list_employ:
        if employ >= average_happiness:
            sorted_happiness_list.append(employ)
    counts_happy_people = len(sorted_happiness_list)
    return sorted_happiness_list, counts_happy_people


employees = input().split()
happiness_factor = int(input())
sorted_list, counter_people = employees_happiness(employees, happiness_factor)
if len(employees) / 2 <= counter_people:
    print(f"Score: {counter_people}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {counter_people}/{len(employees)}. Employees are not happy!")
