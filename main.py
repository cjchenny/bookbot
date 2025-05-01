
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

text = get_book_text("./books/frankenstein.txt")

def get_word_count(text):
    split_words = text.split()
    return len(split_words)

def main():
    print(f"{get_word_count(text)} words found in the document")    

main()

