def print_upper_words(list):
    for item in list:
        print(item.upper())

def print_upper_words2(list):
    for item in list:
        if item.startswith('h') or item.startswith('H'):
            print(item.upper())

def print_upper_words3(list, must_start_with):
    for item in list:
        for letter in must_start_with:
            if item.startswith(letter):
                print(item.upper())
                break


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with="y")