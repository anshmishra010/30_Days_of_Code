# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
d={}

for i in range(n):
    data = list(input().rstrip().split())
    d[data[0]] = data[1]
d_keys = d.keys()

while True:
    try:
        name = input()
        if name in d_keys:
            print(name+"="+d[name])
        else:
            print("Not found")
    except:
        break
