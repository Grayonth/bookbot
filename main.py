def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
def count_words(book_texts):
    words = book_texts.split()
    count = len(words)
    return count
def count_chars(book_texts):
    book_texts = book_texts.lower()
    char_count = {}
    for char in book_texts:
         if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count
def report(word_count,char_count):
    sorted_chars = sorted(char_count.items(), key = lambda item: item[1],reverse=True)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print(f"--- End report ---")
book_texts = main()
word_count = count_words(book_texts)
char_count = count_chars(book_texts)
report(word_count,char_count)
