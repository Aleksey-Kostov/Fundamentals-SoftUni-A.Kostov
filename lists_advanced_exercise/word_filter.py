def even_text(text_list):
    even_text_list = [text for text in text_list if len(text) % 2 == 0]
    return even_text_list


some_text = input().split()
print("\n".join(even_text(some_text)))
