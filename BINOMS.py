def Newton(n,k):
    if k==0:
        return 1
    elif k<0:
        return 0
    elif n<(k<<1):
        return Newton(n,n-k)
    wynik = n
    for i in range(2,k+1):
        n -= 1
        wynik*=n
        wynik/=i
    return wynik

t = int(input())
while t:
    a,b = input().split()
    print(int(Newton(int(a),int(b))))
    t-=1
