t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    d={int(x):1 for x in s.split()}
    l=[int(x) for x in s.split()]
    flag=0
    c=0
    for x in range(len(l)):
        for y in range(x+1,len(l)):
            s=l[x]+l[y]
            if (s in d):
                c+=1
                flag=1
    if (flag==1):
        print(c)
    else:
        print(-1)
