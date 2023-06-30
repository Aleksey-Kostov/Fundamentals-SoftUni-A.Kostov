number_of_words = int(input())
words_dict = {}

for i in range(number_of_words):
    main_word = input()
    synonym = input()
    if main_word not in words_dict:
        words_dict[main_word] = []
    words_dict[main_word].append(synonym)

for word in words_dict:
    print(f"{word} - {', '.join(words_dict[word])}")
