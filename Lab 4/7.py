def find_smallest_word(string):
    words = string.split()
    smallest_word = min(words, key=len)
    return smallest_word

string = input("Enter a string: ")
smallest_word = find_smallest_word(string)
print("Smallest word:", smallest_word)