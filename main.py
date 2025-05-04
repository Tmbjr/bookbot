from stats import count_words
from stats import count_characters
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as in_file:
        file_contents = in_file.read()
    return file_contents


def print_report(string):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {string}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(string))} total words")
    print("--------- Character Count -------")

    char_dict = count_characters(get_book_text(string))
    sorted_dict = sort_dictionary(char_dict)

    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])



main()
