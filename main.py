path = "books/frankenstein.txt"

from stats import get_num_words
from stats import count_chars
from stats import sort_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

text = get_book_text(path)
characters = count_chars(text)
sorted_characters = sort_chars(characters)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")    
    print("--------- Character Count -------")
    for char_dict in sorted_characters:
        character = char_dict["char"]
        count = char_dict["num"]

        print(f"{character}: {count}")
    print("============= END ===============")
main()

