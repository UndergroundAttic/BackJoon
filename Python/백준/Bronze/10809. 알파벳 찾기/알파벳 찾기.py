A,i=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],input()
print(" ".join([str(i.index(a))if(a in i)else"-1"for a in A]))