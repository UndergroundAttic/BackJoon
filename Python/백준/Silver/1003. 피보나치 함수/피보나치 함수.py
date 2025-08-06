fibs = [0, 1]
def fib(n):
    while len(fibs) <= n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]
_, *l = [*open(0)]
for i in l:
    i = int(i)
    print(fib(i - 1) if i != 0 else 1, fib(i))
