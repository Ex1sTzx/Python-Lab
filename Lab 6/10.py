def add_ing(string):
    if len(string) < 3:
        return string
    if string.endswith("ing"):
        return string + "ly"
    return string + "ing"

string = "Hello"
result = add_ing(string)
print("Modified string:", result)  # Output: Modified string: Helloing