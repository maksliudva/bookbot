def get_book_text(path):
    """
    Returns book text string
    """
    with open(path) as book:
        text_string = book.read()
    return text_string


def get_chars_dict(text):
    """
    Returns dictionary of alphabetic values
    """
    chars = {}
    for ch in text:
        if not ch.isalpha(): #isalpha() true if alphanumeric symbol
            continue

        lowered = ch.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]


def create_list_from_dict(dict):
    """
    Returns list that contains dictionary elements for every letter
    """
    dictionary_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for ch in alphabet:
        temp_dict = dict.fromkeys(ch,dict[ch])
        temp_dict["num"] = dict[ch]
        dictionary_list.append(temp_dict)  
        
    return dictionary_list


def get_dict_by_key(list_of_dict, key="num"):
    for dict in list_of_dict:
        if dict[key]:
            return dict
    return None


def sort_list(list,key="num"):
    """
    Sorts list by a given criteria
    """
    list.sort(reverse = True, key = lambda d: d.get(key,0))


def count_words(file_string):
    """
    Returns count of words
    """
    words = file_string.split()
    count = 0
    for i in words:
        count = count + 1
    return count


def print_report(text,characters_list,path):
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document")
    for dict in characters_list:
        for k, v in dict.items():
            if k != "num":
                print(f"The '{k}' character was found {v} times")
            


def __main__():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    #print(f"{word_count} words found in the document.")
    #count_characters(book_text)
    #print(get_chars_dict(book_text))
    characters_dict = get_chars_dict(book_text)
    characters_list = create_list_from_dict(characters_dict)
    sort_list(characters_list)
    print_report(book_text,characters_list, filepath)  
    #print(characters_list[0].[0])

if __name__ == '__main__':
    __main__()
    