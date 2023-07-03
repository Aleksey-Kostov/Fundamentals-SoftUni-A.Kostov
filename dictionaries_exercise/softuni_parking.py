number_of_commands = int(input())
parking_car_dict = {}

for commands in range(number_of_commands):
    command = input().split()
    if len(command) == 3:
        name, plate = command[1], command[2]
        if name not in parking_car_dict.keys():
            parking_car_dict[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif len(command) == 2:
        name = command[1]
        if name not in parking_car_dict.keys():
            print(f"ERROR: user {name} not found")
        else:
            del parking_car_dict[name]
            print(f"{name} unregistered successfully")

for name, plate in parking_car_dict.items():
    print(f"{name} => {plate}")
