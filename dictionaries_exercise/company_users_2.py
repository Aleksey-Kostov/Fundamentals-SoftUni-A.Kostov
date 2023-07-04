company = input().split(" -> ")
company_dict = {}

while company[0] != "End":
    company_name, company_id = company[0], company[1]
    if company_name not in company_dict.keys():
        company_dict[company_name] = []
    if company_id not in company_dict[company_name]:
        company_dict[company_name].append(company_id)
    company = input().split(" -> ")

for name, company_number in company_dict.items():
    print(name)
    for number in company_number:
        print(f"-- {number}")
