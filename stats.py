def get_num_words(text):
    split_words = text.split()
    return len(split_words)

def count_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_chars(characters):
    sorted_characters = []

    def sort_on(dict):
        return dict["num"]

    for char, count in characters.items():
        char_info = {"char": char, "num": count}
        if str.isalpha(char) == True:
            sorted_characters.append(char_info)

    sorted_characters.sort(reverse=True, key=sort_on)

    return sorted_characters


