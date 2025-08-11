import sys

N = int(sys.stdin.readline().rstrip())
wset = set()
for i in range(N):
    wset.add(sys.stdin.readline().rstrip())

m = max(map(len, wset))
s = []
for i in range(1, m + 1):
    s.extend(sorted([w for w in wset if len(w) == i]))
print("\n".join(s))
