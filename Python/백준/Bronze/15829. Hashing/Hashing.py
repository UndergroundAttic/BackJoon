R, M, a,S = 31, 123456789, "abcdefghijklmnopqrstuvwxyz",0
L, s = [*open(0)]
for i in range(len(s.strip())):
    S += (a.index(s[i]) + 1) * R**i
print(S)
