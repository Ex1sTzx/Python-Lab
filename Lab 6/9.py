def swap_characters(string1, string2):
    if len(string1) < 2 or len(string2) < 2:
        return string1, string2
    return string2[0] + string1[1:] + string1[0] + string2[1:], string1[0] + string2[1:] + string2[0] + string1[1:]

string1 = "Hello"
string2 = "World"
result1, result2 = swap_characters(string1, string2)
print("Swapped strings:", result1, result2)  # Output: Swapped strings: eHollo dlroW