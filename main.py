from stats import get_num_words
from stats import char_num_times
from stats import sorted_list_of_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as f:
        book = get_book_text(f)  
    dict_num_char = char_num_times(book)
    sorted_list = sorted_list_of_dict(dict_num_char)    
    

    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------\nFound {get_num_words(book)} total words\n--------- Character Count -------")
    print_nicely(sorted_list)
    print("============= END ===============")

def get_book_text(book):
    return book.read()

def print_nicely(sorted_list):
    for pair in sorted_list:
        print(f"{pair["char"]}: {pair["num"]}")

main()
