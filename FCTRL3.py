t = int(input())
while t:
    silnia = 1
    liczba = int(input())
    if liczba<10:
        for i in range(1,liczba+1):
            silnia*=i
    else:
        silnia = 0
    print(str(int(silnia%100/10))+" "+str(silnia%10))
    t-=1
