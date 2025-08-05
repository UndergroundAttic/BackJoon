import sys
L=sys.stdin.readlines()
for l in L:
    print(sum(map(int,l.split())))