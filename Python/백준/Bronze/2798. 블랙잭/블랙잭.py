[N,M],*C=map(lambda x:x.split(),open(0))
M,C=int(M),[*map(int, *C)]
def f(s):
    m = 0
    for a in s:
        for b in s[s.index(a) + 1 :]:
            for c in s[s.index(b) + 1 :]:
                if (d := a + b + c) <= M and d > m:
                    m = d
                    break
    return m
print(f(sorted(C, reverse=True)))