import sys
L=sys.stdin.readlines()
for l in L:
    if "0"in l:
        break
    print(sum(map(int,l.split())))