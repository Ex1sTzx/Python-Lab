def calculate_length(string):
    count = 0
    for _ in string:
        count += 1
    return count

string = "Hello, World!"
length = calculate_length(string)
print("Length of the string:", length)