for i in range(int(input())):
    H,W,N=map(int,input().split());print(f"{H}01"if N==H else f"{H}{N//H:02d}"if N%H==0 else f"{N%H}{N//H+1:02d}")