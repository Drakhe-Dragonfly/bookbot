def get_book_text(relative_path) :
    file_content = ""
    with open(relative_path) as f:
        file_content = f.read()
    return file_content

from stats import word_counting
from stats import characters_counting
from stats import sorted_character_count
import sys



def main():
    argument_list = sys.argv
    relative_path = None
    if len(argument_list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = argument_list[1]
    file_content = get_book_text(relative_path)
    word_count = word_counting(file_content)
    character_count = characters_counting(file_content)
    sorted_count = sorted_character_count(character_count)
    print("============ BOOKBOT ============")
    print(f"analysing book found at {relative_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_count:
        if entry["name"].isalpha() == True:
            print(f"{entry["name"]}: {entry["num"]}")
        else :
            pass
    print("============= END ===============")

main()