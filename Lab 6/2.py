def print_even_numbers():
    count = 0
    num = 0
    while count < 5:
        if num % 2 == 0:
            print(num)
            count += 1
        num += 1

print_even_numbers()