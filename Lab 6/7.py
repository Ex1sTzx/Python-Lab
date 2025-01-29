def get_substring(string):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]

string = "Hello, World!"
substring = get_substring(string)
print("Substring:", substring)