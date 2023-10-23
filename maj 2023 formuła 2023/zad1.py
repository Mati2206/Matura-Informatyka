#3

B = [[10], [8, 15], [4, None, 12, None], [None, 6, None, None, None, 13, None, None], [None for _ in range(2**4)]]

def A(i, j):
    print(B[i][j -1])
    if (B[i+1][2*j-1 -1] is not None):
        A(i + 1, 2*j - 1)
    if (B[i+1][2*j -1] is not None):
        A(i + 1, 2*j)

A(0, 1)
