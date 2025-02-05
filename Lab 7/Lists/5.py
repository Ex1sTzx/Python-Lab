arr = ['abc', 'xyz', 'aba', '1221']
print([s for s in arr if len(s) >= 2 and s[0] == s[-1]])
