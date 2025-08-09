I = [*open(0)]
for i in I:
    if (a := i.strip()) == "0":
        break
    print("yes" if a == a[::-1] else "no")
