a, b = map(int, input().split())
m= 0
if a == b:
    print(a, a, sep="\n")
else:
    for i in range(1, c := max(a, b)):
        if a % i == 0 and b % i == 0 and i > m:
            m = i
    M = int(min(a, b) * c / m)

    print(m, M, sep="\n")
