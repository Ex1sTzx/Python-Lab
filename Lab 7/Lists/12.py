sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [sample_list[i] for i in range(len(sample_list)) if i not in [0, 4, 5]]
print(new_list)