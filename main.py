from stats import get_number_of_words, get_char_count, sort_characters, sort_on
import sys


def get_book_text(filepath):
    with open(filepath) as book:
        book_content = book.read()
    return book_content    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]     
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = sort_characters(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")
main()