t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    m=int(input())
    l=[int(x) for x in s.split()]
    l.sort()
    sm=10**18
    for x in range(n-m+1):
        if (l[m-1]-l[x]<sm):
            sm=l[m-1]-l[x]
        if sm==0:
            break
        m+=1
    print(sm)
