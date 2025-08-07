N = int(input())
s = 0
for i in range(N):
    if sum(map(int, str(i)), i) == N:
        print(i)
        s = 1
        break
if s == 0:
    print(0)
