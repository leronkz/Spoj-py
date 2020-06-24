p = int(input())
while p:
    suma = 0
    n = int(input())
    t = []
    t = input().split()
    for i in range(n):
        suma=suma+int(t[i])
    print(suma)
    p=p-1
