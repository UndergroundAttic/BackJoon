I = [*open(0)]
for i in I:
    a, b, c = sorted(map(int, i.split()))
    if a | b | c == 0:
        break
    print("right" if a**2 + b**2 == c**2 else "wrong")