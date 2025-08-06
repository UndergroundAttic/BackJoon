l,s=[*open(0)],set()
for i in l:
    s.add(int(i)%42)
print(len(s))
