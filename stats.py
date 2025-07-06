def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    char_count = {}
    words = text.split()
    for word in words:
        for char in word:
            char = char.lower()
            if (char in char_count):
                char_count[char] += 1
            else:
                char_count[char] = 1 
    return char_count

def criteria(d):
    return d["count"]

def sort_dict(chars):
    list_of_dicts = []
    for char in chars:
        c = {"char":char, "count":chars[char]}
        list_of_dicts.append(c)
    list_of_dicts.sort(reverse=True, key=criteria)
    return list_of_dicts