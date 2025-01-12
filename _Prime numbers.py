#enter a number and the program will return all the prime numbers before that number (including the inserted number)
a = int(input("Value : "))
for b in range(2, a+1):
    v = True
    for c in range(2, b):
        d = b % c
        if d == 0: v = False
    if v == True: print(b)
