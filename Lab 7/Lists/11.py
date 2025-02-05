def common(list1, list2):
    common = set(list1) & set(list2)
    if common:
        return True
    else:
        return False

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common(list1, list2)
print(result)