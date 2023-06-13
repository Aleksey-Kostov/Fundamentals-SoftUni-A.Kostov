def recoding_messages(input_message: list):
    deciphered = []
    for message in input_message:
        ascii_char = [digit for digit in message if digit.isdigit()]
        word_list = [digit for digit in message if digit not in ascii_char]
        number = chr(int("".join(ascii_char)))
        word_list[0], word_list[-1] = word_list[-1], word_list[0]
        new_word = number + "".join(word_list)
        deciphered.append(new_word)
    return deciphered


secret_messages = input().split()
new_secret_message = recoding_messages(secret_messages)
print(" ".join(new_secret_message))
