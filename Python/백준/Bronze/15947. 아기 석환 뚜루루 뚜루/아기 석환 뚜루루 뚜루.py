a, b, N = "baby", "sukhwan", int(input()) - 1
m = {0: a, 12: a, 1: b, 13: b, 4: "very", 5: "cute", 8: "in", 9: "bed"}

if (l := N % 14) in m:
    print(m[l])
elif (t := N // 14) > 2 and l % 2 == 0:
    print(f"tu+ru*{t+2}")
elif l % 2 == 0:
    print("tu" + "ru" * (t + 2))
elif t > 3:
    print(f"tu+ru*{t+1}")
else:
    print("tu" + "ru" * (t + 1))
