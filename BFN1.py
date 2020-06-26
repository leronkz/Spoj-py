def odwroc(a):
    c = ""
    while a>0:
        c+=str(a%10)
        a/=10
        a = int(a)
    b = int(c)
    return b
def czy_palindrom(a):
    t = True
    b = str(a)
    for i in range(int(len(b)/2)):
        if b[i]==b[len(b)-i-1]:
            t = True
        else:
            t = False
            break
    return t
t = int(input())
while t:
    a = int(input())
    ile = 0
    while not(czy_palindrom(a)):
        b = odwroc(a)
        a = a+b
        ile+=1
    print(a,ile)
    t-=1
