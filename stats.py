def get_number_of_words(book_content):
    words = book_content.split()
    num_words = len(words)
    return num_words

def get_char_count(book_content):
    char_count = {}
    for ch in book_content:
        ch = ch.lower()
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count

def sort_on(character_dict):
    return character_dict["num"]

def sort_characters(character_dict):
    char_list=[]
    for ch, count in character_dict.items():
        key = {"char": ch, "num": count}
        char_list.append(key)
    char_list.sort(reverse=True, key=sort_on)
    return char_list