def find_longer_words(word_list, n):
    longer_words = [word for word in word_list if len(word) > n]
    return longer_words

sample_list = ["apple", "banana", "cherry", "date", "fig"]
n = 4
result = find_longer_words(sample_list, n)
print(result)