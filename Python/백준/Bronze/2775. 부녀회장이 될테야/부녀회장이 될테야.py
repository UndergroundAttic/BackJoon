N = int(input())

def live(k, n, mat=None):
    if not mat:
        mat = [[0] * (n + 1) for _ in range(k + 1)]
    if k == 0:
        return n
    else:
        if mat[k][n] == 0:
            mat[k][n] = sum([live(k - 1, i, mat) for i in range(1, n + 1)])
        return mat[k][n]

for i in range(N):
    k, n = int(input()), int(input())
    print(live(k, n))