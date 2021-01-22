def pr(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0): return False
    return True
x=int(input())
for i in range(x):
    a=int(input())
    if pr(a): print("Prime")
    else: print("Not prime")