t=int(input())
for _ in range(t):
    s=input()
    l=[int(x) for x in s.split()]
    n=l[0]
    k=l[1]
    s=input()
    l=[int(x) for x in s.split()]
    sm=l[0]-k
    l2=[]
    p=0
    if (sm<0):
        sm=sm*-1
    for x in l:
        d=x-k
        if (d<0):
            d=d*-1
        if (d<sm):
            sm=d
            p=x
        elif (d==sm):
            if(x>p):
                p=x
    print(p)
