while "0" not in (l := input().split()):
    print(["No", "Yes"][int(l[0]) > int(l[1])])
