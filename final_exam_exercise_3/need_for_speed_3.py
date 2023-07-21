number_of_cars = int(input())
model_cars_dict = {}
sum_fuel = 0

for car in range(number_of_cars):
    model_car = input().split("|")
    model, mileage, fuel = model_car[0], int(model_car[1]), int(model_car[2])
    if model not in model_cars_dict:
        model_cars_dict[model] = [mileage, fuel]
    else:
        model_cars_dict[model][0] += mileage
        model_cars_dict[model][1] += fuel

command = input().split(" : ")

while command[0] != "Stop":
    if command[0] == "Drive":
        car_command, distance, fuel = command[1], int(command[2]), int(command[3])
        if model_cars_dict[car_command][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            model_cars_dict[car_command][1] -= fuel
            model_cars_dict[car_command][0] += distance
            print(f"{car_command} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if model_cars_dict[car_command][0] >= 100000:
                del model_cars_dict[car_command]
                print(f"Time to sell the {car_command}!")
    elif command[0] == "Refuel":
        car_command, fuel = command[1], int(command[2])
        sum_fuel = model_cars_dict[car_command][1] + fuel
        if sum_fuel > 75:
            diff_fuel = 75 - model_cars_dict[car_command][1]
            model_cars_dict[car_command][1] = 75
        else:
            model_cars_dict[car_command][1] += fuel
            diff_fuel = fuel
        print(f"{car_command} refueled with {diff_fuel} liters")
    elif command[0] == "Revert":
        car_command, kilometers = command[1], int(command[2])
        model_cars_dict[car_command][0] -= kilometers
        if model_cars_dict[car_command][0] < 10000:
            model_cars_dict[car_command][0] = 10000
        else:
            print(f"{car_command} mileage decreased by {kilometers} kilometers")
    command = input().split(" : ")

for car_dict, resource in model_cars_dict.items():
    print(f"{car_dict} -> Mileage: {model_cars_dict[car_dict][0]} kms,"
          f" Fuel in the tank: {model_cars_dict[car_dict][1]} lt.")
