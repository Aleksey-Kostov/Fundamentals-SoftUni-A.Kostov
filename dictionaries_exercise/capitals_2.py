country_names = input().split(", ")
capitals = input().split(", ")
country_dict = {country_names[i]: capitals[i] for i in range(len(country_names))}
for names, capital in country_dict.items():
    print(f"{names} -> {capital}")

