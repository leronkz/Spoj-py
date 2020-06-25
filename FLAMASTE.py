t = int(input())
while t:
    s = input()
    s_2 = ""
    licznik = 1
    temp = s[0]
    for i in range(1,len(s)):
       if temp == s[i]:
           licznik+=1
       elif temp != s[i] or i == len(s):
           if licznik<2:
               s_2+=temp
           elif licznik==2:
               s_2+=temp
               s_2+=temp
           elif licznik>=3:
               s_2+=temp
               s_2+=str(licznik)
           licznik = 1
           temp = s[i]
           i-=1
    if licznik!=0:
        if licznik>=3:
            s_2+=temp
            s_2+=str(licznik)
        else:
            for i in range(licznik):
                s_2+=temp
    print(s_2)
    t = t-1
