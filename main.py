def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


frankenstein = main()

print(frankenstein)