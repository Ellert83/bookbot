from stats import *
import sys

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


# print(f"{count_words(get_book_text(path))} words found in the document")
# print(char_count(get_book_text(path)))
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]

dict = sort_dict(get_book_text(path))
result = ""
for letter, count in dict:
    if letter.isalpha():
        result += (f"{letter}: {count}\n")
print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {count_words(get_book_text(path))} total words
--------- Character Count -------
{result}
============= END ===============
"""
)
