def nwd(a,b):
    while a!=b:
        if a > b:
            a-=b
        else:
            b-=a
    return a

def nww(a,b):
    c = a*b/nwd(a,b)
    return c

t = int(input())

while t:
    a,b = input().split()
    print(int(nww(int(a),int(b))))
    t-=1
