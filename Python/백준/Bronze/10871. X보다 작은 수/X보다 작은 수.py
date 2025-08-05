x, l = int(input().split()[-1]), map(int, input().split())
print(" ".join(str(i) for i in l if i < x))