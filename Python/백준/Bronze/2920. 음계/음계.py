print("ascending"if(y:=sorted(x:=input().split()))==[*x]else"descending"if(z:=sorted(x,reverse=1))==[*x]else"mixed")
