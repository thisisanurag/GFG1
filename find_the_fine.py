t=int(input())
for _ in range(t):
    s=input()
    l=[int(x) for x in s.split()]
    n=l[0]
    d=l[1]
    s=input()
    c=[int(x) for x in s.split()]
    s=input()
    p=[int(x) for x in s.split()]
    t=0
    if (d%2==0):
        for x in range(n):
            if (c[x]%2!=0):
                t=t+p[x]
    else:
        for x in range(n):
            if(c[x]%2==0):
                t=t+p[x]
    print(t)
