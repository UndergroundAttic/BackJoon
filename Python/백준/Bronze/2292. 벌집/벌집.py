t, N = 1, int(input())
for a in range(N):
    t += 6 * a
    if t >= N:
        print(a + 1)
        break