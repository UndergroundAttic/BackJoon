N, I = [*open(0)]
I = [*map(int, I.split())]
M = max(I)
print(sum([*map(lambda x: 100 * x / M, I)]) / len(I))