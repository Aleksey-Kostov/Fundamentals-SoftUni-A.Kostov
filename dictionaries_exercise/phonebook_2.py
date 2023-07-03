command = input()
phonebook_dict = {}

while "-" in command:
    name, number = command.split("-")
    if name not in phonebook_dict.keys():
        phonebook_dict[name] = 0
    phonebook_dict[name] = number
    command = input()

for contacts in range(int(command)):
    name_contacts = input()
    if name_contacts not in phonebook_dict.keys():
        print(f"Contact {name_contacts} does not exist.")
    else:
        print(f"{name_contacts} -> {phonebook_dict[name_contacts]}")



