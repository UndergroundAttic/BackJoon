T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        print((a % 10) ** (b % 4 + 4) % 10)
