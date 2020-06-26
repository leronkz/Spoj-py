def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

t = int(input())
while t:
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(nwd(a,b))
    t-=1
