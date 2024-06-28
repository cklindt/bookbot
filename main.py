def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def get_char_dict(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def alpha_dict(dict):
    alpha_dict = {}
    for char in dict:
        if char.isalpha(): 
            alpha_dict[char] = dict[char]
    return alpha_dict
def list_dict(dict):
    list_dict = []
    for char in dict:
        list_dict.append({"char": char, "num":dict[char]})
    return list_dict

def sort_on(dict):
    return dict["num"]

def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document")
    chars = get_char_dict(text)
    chars = alpha_dict(chars)
    dict_list_chars = list_dict(chars)
    dict_list_chars.sort(reverse=True, key=sort_on)
    for dict in dict_list_chars:
        print(f"The {dict['char']} character was found {dict['num']} times")
    print("--- End report ---")

main()
