def palindrome_string(word_list, search):
    new_palindrome_list = []
    for word in word_list:
        if word == word[::-1]:
            new_palindrome_list.append(word)
    return new_palindrome_list, new_palindrome_list.count(search)


words = input().split()
searched_palindrome = input()
total_palindrome_list, count_palindrome = palindrome_string(words, searched_palindrome)

print(total_palindrome_list)
print(f"Found palindrome {count_palindrome} times")
