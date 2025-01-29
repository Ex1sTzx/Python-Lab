def capitalize_words(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

string = input("Enter a string: ")
capitalized_string = capitalize_words(string)
print("Capitalized string:", capitalized_string)