from stats import get_word_count, count_chars, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    text = get_book_text(path_to_book)
    word_count = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_count = count_chars(text)

    sorted_by_count = sort_dict(char_count)
    for d in sorted_by_count:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['count']}")

main()