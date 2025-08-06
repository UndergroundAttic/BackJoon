a=input()
s,c=int(a)%7==0,"7"in a
print(3 if s and c else 2 if c else 1 if s else 0)