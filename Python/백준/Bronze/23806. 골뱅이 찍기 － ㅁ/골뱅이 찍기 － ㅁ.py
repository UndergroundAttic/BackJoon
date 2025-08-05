i,A,B=int(input()),"@"," "
l=5*i
for _ in range(i):
    print(l*A)
for _ in range(l-2*i):
    print(i*A+(l-2*i)*B+i*A)
for _ in range(i):
    print(l*A)