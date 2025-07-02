def word_count(text):
    words = text.split()
    return(len(words))

def count_chars(text):
    lowercased = text.lower()
    chars = {}
    for char in lowercased:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def get_book_text(path):
    with open(f'{path}', 'r', encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def print_report(dict):
    dict = convert_to_list(dict)
    dict.sort(reverse = True, key=sort_on)
    for chars in dict:
        if chars['char'].isalpha():
            print(f"{chars['char']}: {chars['num']}")
    print("---End report---")

def convert_to_list(dicts):
    dicts_list = []
    for char in dicts:
        new_dict = {'char': char, 'num': dicts[char]}
        dicts_list.append(new_dict)
    return dicts_list

def sort_on(dict):
    return dict["num"]
