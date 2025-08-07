_, N = [*open(0)]
N = [i for i in map(int, N.split()) if i > 1]
M = max(N) + 1
for i in range(2, M):
    N = [n for n in N if (n % i != 0 or n == i)]
print(len(N))
