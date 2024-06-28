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
    text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{word_count(text)} words found in the document")

main()
