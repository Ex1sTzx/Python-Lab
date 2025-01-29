def find_common_words(string1, string2):
    words1 = set(string1.lower().split())
    words2 = set(string2.lower().split())
    common_words = words1.intersection(words2)
    return common_words

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
common_words = find_common_words(string1, string2)
print("Common words:", common_words)