a,b,c=open(0)
print("Deletion",["succeeded","failed"][any(int(a)%2^(i!=j)for i,j in zip(b,c[:-1]))])