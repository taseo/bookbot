import sys

def sort_on(dict):
    return dict["count"]

def print_report(path_to_file, word_count, characters):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print(" ")
    
    character_list = [{'character': key, 'count': value} for key, value in characters.items()]
    
    character_list.sort(reverse=True, key=sort_on)

    for item in character_list:
        print(f"The '{item['character']}' character was found {item['count']} times")

    print("--- End report ---")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
        return 1

    path_to_file = sys.argv[1]

    try:
        with open(path_to_file) as f:
            file_contents = f.read()

            words = file_contents.split()

            characters = {}

            for word in words:
                for c in word:
                    if c.isalpha():
                        normalized_character = c.lower()

                        if normalized_character in characters:
                            characters[normalized_character] = characters[normalized_character] + 1
                        else:
                            characters[normalized_character] = 1

            print_report(path_to_file, len(words), characters)

    except FileNotFoundError:
        print(f"File '{path_to_file}' not found")
        return 1

    except IsADirectoryError:
        print(f"'{path_to_file}' is a directory. Please provide a file.")
        return 1

if __name__ == '__main__':
    sys.exit(main())