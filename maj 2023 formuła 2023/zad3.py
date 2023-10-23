
f = open('./Dane_2305/pi.txt', "r")
pi = f.read().replace('\n', '')

def fragments(pi, k):
    m = 0
    for i in range(len(pi) - k + 1):
        if int(pi[i:i+k]) > 90:
            m += 1
    return m

def fragments_count(pi, k):
    tab = [0 for _ in range(100)]
    for i in range(len(pi) - k + 1):
        tab[int(pi[i:i+k])] += 1
    
    for i in range(len(tab)):
        if (tab[i] == 80):
            print(80, i)
        elif(tab[i] == 124):
            print(124, i)

    return (tab.index(min(tab)), min(tab)), (tab.index(max(tab)), max(tab))




                
def check_growing_descending(n):
    grow = True
    if (n[0] >= n[1] or n[-2] <= n[-1]):
        return False
    for i in range(len(n) - 1):
        if ((n[i] < n[i+1] or n[i] == n[i+1]) and not grow):
            return False
        elif (n[i] >= n[i+1]):
            grow = False
    if (not grow):
        return True
    return False

m = 0
p = 0
for j in range(3, 12):
    for i in range(len(pi) - j - 1):
        x = check_growing_descending(pi[i:i+j])
        if(x):
            m = pi[i:i+j]
            p = i+1
            break
print(m, p)
