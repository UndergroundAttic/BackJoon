from math import ceil
t = input()
for i in range(int(t)):
    n, c = map(int, input().split())
    print(ceil(n / c))
