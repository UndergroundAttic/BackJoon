i=[*open(0)]
(n,d),t=map(int,i[0].split()),list(map(int,i[1:]))
[print(int(d*x/sum(t)))for x in t]