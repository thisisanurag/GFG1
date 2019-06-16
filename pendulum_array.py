t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    lis=[int(x) for x in s.split()]
    f=0
    if (n%2==0):
        r=int((n-1)/2)+1
        l=int((n-1)/2)-1
    else:
        r=int(n/2)+1
        l=int(n/2)-1
    a=[0]*n
    for x in range(n):
        sm=min(lis)
        lis.remove(sm)
        if (x==0 and n%2==0):
            a[int((n-1)/2)]=sm
        elif(x==0 and n%2!=0):
            a[int(n/2)]=sm
        elif(f==0 ):
            a[r]=sm
            r+=1
            f=1
        elif(f==1 ):
            a[l]=sm
            l-=1
            f=0
    print(' '.join(map(str, a)))
