memo = int(input())
idx = 1
def c(i):
    return i / 2 if i % 2 == 0 else i * 3 + 1
while memo != 1:
    memo = c(memo)
    idx += 1
print(idx)
