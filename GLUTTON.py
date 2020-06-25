from math import floor
from math import ceil
t = int(input())
while t:
    n,m = input().split()
    czasy = []
    for i in range(int(n)):
        x = int(input())
        czasy.append(x)
    ile_ciastek = 0
    ile_pudelek = 0
    for i in range(int(n)):
        ile_ciastek+=floor(86400/czasy[i])
    ile_pudelek = ile_ciastek/int(m)
    print(ceil(ile_pudelek))
    t-=1
