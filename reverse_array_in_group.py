#Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.
t=int(input())
for _ in range(t):
    s=input()
    l=[int(x) for x in s.split()]
    n=l[0]
    g=l[1]
    s=input()
    l=[int(x) for x in s.split()]
    l2=[]
    c=1
    for x in range(n):
        if c%(g+1)!=0:
            l2.append(l[x])
            c+=1
        else:
            l2.reverse()
            for y in l2:
                print(y,end=' ')
            l2=[]
            l2.append(l[x])
            c=2
    if (l2):
        l2.reverse()
        for y in l2:
            print(y,end=' ')
    print()
            
