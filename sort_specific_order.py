t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=[int(x) for x in s.split()]
    l2=[]
    l3=[]
    for x in l:
        if x%2==0:
            l2.append(x)
        else:
            l3.append(x)
    l3.sort(reverse=True)
    l2.sort()
    p1=' '.join(map(str, l3))
    p2=' '.join(map(str, l2))
    print(p1,end=' ')
    print(p2,end=' ')
    print()
