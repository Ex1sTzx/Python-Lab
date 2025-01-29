def is_palindrome(string):
    string = string.lower()
    string = ''.join(c for c in string if c.isalnum())
    return string == string[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")