s = [*open(0)][1:]
for a in s:
    p, P = 0, 0
    for c in a:
        if c == "O":
            p += 1
            P += p
        else:
            p = 0
    print(P)
