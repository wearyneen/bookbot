#main - print the book
def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_num_words(text)
    character_count = letter_count(text)
    print_report(book_path, word_count, character_count)

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
    
def clean_character(character_dictionary):
    pass
    
def print_report(path, word_count, character_count):

    print(f"---Report for {path}---")
    print()
    print(f"{word_count} number of in the book.")
    print()
    for character in character_count:
        if character.isalpha():
            print(f"There are {character_count[character]} {character}'s in this book" )
    print()
    print("---End---")

main()
