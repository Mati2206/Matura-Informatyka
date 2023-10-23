def check_two(l):
    pow = 0
    while True:
        if (2**pow > l):
            return pow
        pow+=1

def dec_to_bin(l):
    pow = check_two(l)
    m = ""
    while pow >= 0:
        if (2**pow <= l):
            m += "1"
            l -= 2**pow
        elif (m != ""):
            m += "0"
        pow -= 1
    return m

def dec_to_bin_modify(l):
    pow = check_two(l)
    block = 1
    block1 = 1
    block2 = 0
    m = ""
    while pow >= 0:
        if (2**pow <= l):
            m += "1"
            if (block == 0):
                block = 1
                block1 += 1
            l -= 2**pow
        elif (m != ""):
            m += "0"
            if (block == 1):
                block = 0
                block2 += 1
        pow -= 1
    return [m, block1, block2]

def bin_modify():
    f = open('./Dane_2305/bin.txt', 'r')
    m = 0
    for i in f.readlines():
        x = i[:-1]
        block = 1
        block1 = 1
        block0 = 0
        for j in x:
            if (j == '1' and block == 0):
                block = 1
                block1 += 1
            elif (j == '0' and block == 1):
                block = 0
                block0 += 1
        if (block1 + block0 <= 2):
            m+= 1
    print(m)

def maxbin():
    f = open('./Dane_2305/bin.txt', 'r')
    m = 0
    for i in f.readlines():
        x = i[:-1]
        if (int(str(m), 2) < int(x, 2)):
            m = x
    print(m)

def xor(p, q):
    while len(p) != len(q):
        if (len(p) < len(q)):
            p = '0' + p
        else:
            q = '0' + q
    m = ""
    for i in range(len(p)):
        if (p[i] == q[i]):
            m += '0'
        else:
            m += '1'
    return m
        


def xor_full():
    f = open('./Dane_2305/bin.txt', 'r')
    o = open('./wyniki2_5.txt', "a")
    for i in f.readlines():
        x = i[:-1]
        o.write(xor(x, dec_to_bin(int(x, 2)//2))+"\n")


xor_full()
