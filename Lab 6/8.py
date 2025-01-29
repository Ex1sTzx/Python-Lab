def change_first_char(string):
    if len(string) < 2:
        return string
    return '$' + string[1:]

string = "Hello, World!"
new_string = change_first_char(string)
print("New string:", new_string)