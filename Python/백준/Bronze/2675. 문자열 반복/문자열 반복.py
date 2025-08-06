s=[*open(0)][1:]
for i in s:
    S=""
    for j in (x:=i.split())[1]:
        S+=j*int(x[0])
    print(S)
