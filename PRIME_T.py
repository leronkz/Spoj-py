from math import sqrt
n = int(input())
while n > 0:
    a = int(input())
    if a == 1:
        print("NIE")
    elif a == 2:
        print("TAK")
    else:
        g = int(sqrt(a))
        t = True
        for i in range(2,g+1):
            if a % i == 0:
                t = False
                break
            else:
                t = True
        if t:
            print("TAK")
        else:
            print("NIE")
    n -= 1

