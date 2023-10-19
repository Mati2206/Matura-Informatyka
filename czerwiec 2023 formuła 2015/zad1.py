def myStr(a):
    tab = []
    m = 0
    while a >= 10:
        tab.append(a%10)
        m += 1
        a //= 10
    tab.append(a)
    return tab, m

def dobre_przyjaciolki(a, b):
    a, ma = myStr(a)
    b, mb = myStr(b)
    suma, sumb = 0, 0
    for i in a:
        suma += i
    for i in b:
        sumb += i 
    if ((a[0] == b[mb] or b[0] == a[ma]) and suma == sumb):
        return True
    return False
    
print(dobre_przyjaciolki(32, 221))