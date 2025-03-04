def count_words(text):
    return len(text.split())

def char_count(text):
    text_lower = list(text.lower())
    char_dict = {}
    for letter in text_lower:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict

def sort_dict(text):
    list_dict = list(char_count(text).items())
    list_dict.sort(reverse=True, key=lambda item: item[1])
    return list_dict

