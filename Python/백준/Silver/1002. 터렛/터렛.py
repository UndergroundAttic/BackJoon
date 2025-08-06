P,*L=[*open(0)]
for l in L:
    x,y,r,X,Y,R=map(int, l.split())
    d=(x-X)**2+(y-Y)**2
    s,S=abs(r-R)**2,(r+R)**2
    if d==0:
        print(-1 if r==R else 0)
    elif S<d or s>d:
        print(0)
    elif S==d or s==d:
        print(1)
    else:
        print(2)