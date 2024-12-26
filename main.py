#main - print the book
def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_num_words(text)
    print(word_count)

#translete str to list and count
def get_num_words(text):
    words = text.split()
    return len(words)

#get book
def get_book(path):
    with open(path) as f:
        return f.read()

main()
