import sys

N = int(sys.stdin.readline().strip())
l = {}
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x in l:
        l[x] += 1
    else:
        l[x] = 1
for i in range(max(l.keys()) + 1):
    if i not in l:
        continue
    for _ in range(l[i]):
        print(i)
