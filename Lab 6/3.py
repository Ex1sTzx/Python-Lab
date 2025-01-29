def print_even_numbers():
    count = 0
    num = 0
    while count < 4:
        num += 1
        if num % 2 != 0:
            continue
        print(num)
        count += 1

print_even_numbers()