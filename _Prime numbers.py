#insérez un nombre et le programme vous renverra tout les nombres premiers avant ce nombre (et le nombre inséré compris)
a=int(input("Value : "))
b=1
while b!=a:
    b=b+1
    c=1
    d=1
    while d!=0:
        c=c+1
        d=b%c
        #print(b,c,d)
        if b==c:
            print(b)
