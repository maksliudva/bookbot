def get_book_text(path):
    """
    Returns book text string
    """
    with open(path) as book:
        text_string = book.read()
    return text_string



def count_words(file_string):
    """
    Returns count of words
    """
    words = file_string.split()
    count = 0
    for i in words:
        count = count + 1
    return count


def __main__():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document.")

if __name__ == '__main__':
    __main__()
    