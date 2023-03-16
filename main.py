import string

book_path = 'books/frankenstein.txt'

with open(book_path, 'r') as file:
    text = file.read()

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_letters(text, sort=True):
    alpha_dict = {
        letter: 0 for letter in string.ascii_lowercase
    }
    for letter in text.lower():
        if letter in alpha_dict:
            alpha_dict[letter] += 1
    if sort:
        return dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    else:
        return alpha_dict

def report(text, path):
    print(f"--- Begin report for {path} ---")
    print(f'{count_words(text)} found in the document')
    print()
    for k,v in count_letters(text).items():
        print(f'The {k} character was found {v} times')
    # print(f'Letter count: {count_letters(text)}')
    print(f"--- End report ---")


# print(count_words(text))
# print(count_letters(text))

report(text, book_path)