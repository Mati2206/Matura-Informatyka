def iloczyn(x, y):
    z = 0
    m = 0
    while (y > 0):
        m += 1
        print(m)
        if (y % 2 == 1):
            z = z + x
        x = x + x
        y = y // 2
    return z

print(iloczyn(10, 45))