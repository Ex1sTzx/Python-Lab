def count_characters(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = "Hello, World!"
frequency = count_characters(string)
print("Character frequency:", frequency)