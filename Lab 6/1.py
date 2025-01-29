def find_smallest_even_number():
    num = 0
    while num < 10:
        if num % 2 == 0:
            print(num)
            break
        num += 1
    else:
        print("No even number found.")

find_smallest_even_number()