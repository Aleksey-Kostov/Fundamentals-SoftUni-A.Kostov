number_of_pieces = int(input())
pieces_dict = {}

for pieces in range(number_of_pieces):
    info_pieces = input().split("|")
    piece = info_pieces[0]
    composer = info_pieces[1]
    key = info_pieces[2]
    pieces_dict[piece] = [composer, key]

command = input().split("|")
while command[0] != "Stop":
    action = command[0]
    if action == "Add":
        piece_from_command = command[1]
        composer_from_command = command[2]
        key_from_command = command[3]
        if piece_from_command not in pieces_dict:
            pieces_dict[piece_from_command] = [composer_from_command, key_from_command]
            print(f"{piece_from_command} by {composer_from_command} in {key_from_command} added to the collection!")
        else:
            print(f"{piece_from_command} is already in the collection!")
    elif action == "Remove":
        piece_from_command = command[1]
        if piece_from_command not in pieces_dict:
            print(f"Invalid operation! {piece_from_command} does not exist in the collection.")
        else:
            del pieces_dict[piece_from_command]
            print(f"Successfully removed {piece_from_command}!")
    elif action == "ChangeKey":
        piece_from_command = command[1]
        new_key = command[2]
        if piece_from_command not in pieces_dict:
            print(f"Invalid operation! {piece_from_command} does not exist in the collection.")
        else:
            pieces_dict[piece_from_command][1] = new_key
            print(f"Changed the key of {piece_from_command} to {new_key}!")
    command = input().split("|")

for current_pieces, items in pieces_dict.items():
    piece = current_pieces
    composer = items[0]
    key = items[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
