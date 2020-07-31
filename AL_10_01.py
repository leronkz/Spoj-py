from math import pow
t = int(input())
while t:
    n,s = input().split()
    n = int(n)
    count=1
    if n == 1 and s == "?":
        print(10)
    elif n==1 and s !="?":
        print(1)
    else:
        for i in range(len(s)):
            if s[i] == '?' and i!=0:
                count*=10
            elif s[i] == '?' and i==0:
                count*=9
        print(int(count))
    t-=1
