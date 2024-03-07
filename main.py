import collections


def main():
    try:
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        counted_words = word_count(text)
        counted_chars = char_count(text)
        print(char_report(counted_chars, counted_words, book_path))
        #print(text)
        #print(counted_words)
        #print(counted_chars)
    except (TypeError, ValueError, PermissionError, FileNotFoundError) as e:
            print(f"Error: {e}")

def word_count(text):
    check_str_empty(text)
    return len((text).split())

def get_book_text(path):
    try:
        check_str_empty(path)
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The document at {path} was not found. Please ensure the file path is correct.")
    except PermissionError:
        raise PermissionError(f"You do not have permission to access {path}, talk to your system adminstaror")
    
def char_count(text):
    #counted_chars = {}
    check_str_empty(text)
    low_text = text.lower()
    return collections.Counter(low_text)
"""
    for i in text:
        low_text = i.lower()
        if low_text in counted_chars:
            counted_chars[low_text] += 1
        else:
            counted_chars[low_text] = 1
    return counted_chars
"""

def char_report(counted_chars, counted_words, book_path):
    print(f"--- Begin report of {book_path} ---\n{counted_words} words found in the document\n")
    sorted_char = dict(sorted(counted_chars.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_char:
        if i.isalpha() == True:
            print (f"The '{i}' character was found {counted_chars[i]} times")
    return("--- End report ---")

def check_str_empty(string):
    if not isinstance(string, str):
        raise TypeError("Expected argument text to be a string")
    if not string:
        raise ValueError("Provided text was empty")
main()