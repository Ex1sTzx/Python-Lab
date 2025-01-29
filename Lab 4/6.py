def count_vowels(string):
    vowels = 'aeiou'
    string = string.lower()
    vowel_count = {vowel: string.count(vowel) for vowel in vowels}
    return vowel_count

string = input("Enter a string: ")
vowel_count = count_vowels(string)
print("Vowel count:", vowel_count)