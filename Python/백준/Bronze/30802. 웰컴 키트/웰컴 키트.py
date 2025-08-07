N,S,_=[*open(0)]
T,P=map(int,_.split())
N=int(N)
print(sum([i//T+1 if(i:=int(s))%T!=0 else i//T for s in S.split()]))
print(N//P,N%P)
