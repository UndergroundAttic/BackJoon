T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    P = int(input())
    system = []
    i = 0
    for _ in range(P):
        system.append(tuple(map(int, input().split())))
    for cx, cy, r in system:
        dsq1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 <= r**2
        dsq2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 <= r**2
        if (dsq1 and not dsq2) or (not dsq1 and dsq2):
            i += 1
    print(i)
