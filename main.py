from stats import get_num_words
from stats import count_chars
from stats import sort_chars
import sys

try:
    path = sys.argv[1]

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

except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
