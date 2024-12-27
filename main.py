#main - print the book
def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_num_words(text)
    character_count = letter_count(text)
    clean_characters = clean_character(character_count)
    print_report(book_path, word_count, clean_characters)

#translete str to list and count
def get_num_words(text):
    words = text.split()
    return len(words)

#create dictionary of characters frequencies
def letter_count(text):
    lower_text = text.lower()
    letter_dict = {}
    for character in lower_text:
        if character in letter_dict:
            letter_dict[character] += 1
        else:
            letter_dict[character] = 1
    return letter_dict 

#get book
def get_book(path):
    with open(path) as f:
        return f.read()
    
def sort_on(d):
    return d["count"]
    
def clean_character(character_dictionary):
    clean_and_sort = []
    for character in character_dictionary:
        if character.isalpha():
            clean_and_sort.append({"character": character, "count": character_dictionary[character]})
    clean_and_sort.sort(reverse=True, key=sort_on)
    return clean_and_sort

def print_report(path, word_count, character_count):

    print(f"---Report for {path}---")
    print()
    print(f"{word_count} number of in the book.")
    print()
    for character in character_count:
        print(f"There are {character["count"]} {character["character"]}'s in this book" )
    print()
    print("---End---")

main()
