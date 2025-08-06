I = [*open(0)][1:]
for i in I:
    print(["ERROR","OK"][(x:=i.split())[0]==x[1]])
