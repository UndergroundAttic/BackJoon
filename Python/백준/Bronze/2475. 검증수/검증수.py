s=input().split()
print(sum([int(x)**2 for x in s])%10)