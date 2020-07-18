t = int(input())

dic = {
    "#000000":"black",
    "#C0C0C0":"silver",
    "#808080":"gray",
    "#FFFFFF":"white",
    "#800000":"maroon",
    "#FF0000":"red",
    "#800080":"purple",
    "#FF00FF":"fuchsia",
    "#008000":"green",
    "#00FF00":"lime",
    "#808000":"olive",
    "#FFFF00":"yellow",
    "#000080":"navy",
    "#0000FF":"blue",
    "#008080":"teal",
    "#00FFFF":"aqua"
}


def zamien(a,b,c):
    a_1 = hex(a)
    b_1 = hex(b)
    c_1 = hex(c)
    a_2 = "0"
    b_2 = "0"
    c_2 = "0"
    if a <= 15:
        a_2 = "0x0"
        a_2+=a_1[2]
    else:
        a_2 = a_1
    if b <= 15:
        b_2 = "0x0"
        b_2 += b_1[2]
    else:
         b_2 = b_1
    if c <= 15:
        c_2 = "0x0"
        c_2+=c_1[2]
    else:
        c_2 = c_1
    l = a_2[2]+a_2[3]
    l += b_2[2]
    l += b_2[3]
    l += c_2[2]
    l += c_2[3]
    return l

while t:
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    s = "#"
    l = zamien(a,b,c)
    l = l.upper()
    s+=l
    try:
        print(dic[s])
    except:
        print(s)
    t-=1
