def iloczyn(x, y):
    if (y == 1):
        return x
    k = int(y/2)
    z = iloczyn(x, k)
    if (y%2 == 0):
        return z+z
    return x+z+z

def iloczyn_zlicz(x, y, l=0):
    if (y == 1):
        return x, l
    k = int(y/2)
    z, l = iloczyn_zlicz(x, k, l)
    if (y%2 == 0):
        l += 1
        return z+z, l
    l += 2
    return x+z+z, l

def iloczyn_interacyjnie(x, y):
    z = x
    while (y > 1):
        print(z, x, y)
        if (y % 2 == 1):
            z = z + x
        x = x + x
        y = int(y/2)
    return z

print(iloczyn_interacyjnie(9, 11))