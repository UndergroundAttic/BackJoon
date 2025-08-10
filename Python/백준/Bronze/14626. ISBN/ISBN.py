seq = input()
m, c = 0, seq[-1]
for i in range(len(seq) - 1):
    char = seq[i]
    if char == "*":
        continue
    else:
        m += int(char) if i % 2 == 0 else int(char) * 3

if seq.index("*") % 2 == 0:
    x = (20 - int(c) - m % 10) % 10
else:
    x = "0369258147".index(str((20 - int(c) - m % 10) % 10))
print(x)